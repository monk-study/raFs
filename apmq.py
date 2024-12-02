-- Create NBA5_FINAL_V2 with additional fields
DROP TABLE IF EXISTS PL_APP_RPHAI.RAW_RPHAI.NBA5_FINAL_V2;
CREATE TABLE PL_APP_RPHAI.RAW_RPHAI.NBA5_FINAL_V2 AS (
SELECT 
    F.*,
    -- Additional Drug Information
    D.LABEL_NM,
    D.GNN_CD,
    D.STRENGTH_CD,
    D.CLASS_CD,
    D.TOP_SELLER_IND,
    D.DRUG_RANK_NBR,
    D.EXPIRE_DAYS_NBR,
    
    -- 30-day Patient History
    PARSE_JSON(PC.REQUEST_JSON):history.history30d.avgPrntPayAmmt::float AS AVG_PAY_30D,
    PARSE_JSON(PC.REQUEST_JSON):history.history30d.prctTimesCdc::float AS CDC_RATE_30D,
    PARSE_JSON(PC.REQUEST_JSON):history.history30d.ttlTimesPaid::int AS TOTAL_PAID_30D,
    
    -- HIC3 Class History
    PARSE_JSON(PC.REQUEST_JSON):history.hic3180d[0].prctTimesPaidCashPrntHic3::float AS HIC3_CASH_RATE,
    PARSE_JSON(PC.REQUEST_JSON):history.hic3180d[0].noOfAttemptsHic3::int AS HIC3_ATTEMPTS,
    PARSE_JSON(PC.REQUEST_JSON):history.hic3180d[0].denialCountHic3::int AS HIC3_DENIALS,
    
    -- Additional Transaction Details
    TX.REFIL_TOO_SOON_ACTIV,
    TX.AUTO_RETRY_IND,
    TX.RQST_CLM_PRIOR_AUTH_CD,
    TX.RQST_CLM_OTHER_COV_CD,
    TX.RQST_PRC_DISPNG_FEE_SUBM_AMT,
    TX.RQST_PRC_GROSS_DUE_AMT,
    
    -- TPRR Specific Information
    TPRR.LOGGING_LIST:model_input.preferred_products::variant as PREFERRED_PRODUCTS,
    TPRR.LOGGING_LIST:rel_codes::variant as REJECTION_CODES,
    TPRR.LOGGING_LIST:msg_in_resp::string as MESSAGE_IN_RESPONSE,
    
    -- Additional Prescription Fill Details
    PF.PATIENT_COUNSEL_CD,
    PF.PHONE_NOTIFICATION_IND,
    PF.PROMISE_DT_CD,
    PF.SOURCE_CD,
    PF.COMPOUND_IND

FROM PL_APP_RPHAI.RAW_RPHAI.NBA5_FINAL F

-- Join with DRUG table for additional drug info
LEFT JOIN CORE_RX.CURATED_PRODUCT.DRUG D
    ON D.NDC = F.NDC

-- Join with PATIENTCARD_JSON_HIST for patient history
LEFT JOIN APP_RPHAI.CURATED_RPHAI.PATIENTCARD_JSON_HIST PC
    ON PC.PATIENTID = F.CVS_CENTR_PAT_NBR
    AND PC.LOAD_DATE = F.PATIENT_HISTORY_LOAD_DATE

-- Join with FACT_NCPDP_ADJ_TXN for transaction details
LEFT JOIN CORE_RX.CURATED_NCPDP.FACT_NCPDP_ADJ_TXN TX
    ON TX.STORE_NBR = F.STORE_NBR
    AND TX.RX_NBR = F.RX_NBR
    AND TX.RX_FILL_NBR = F.FILL_NBR
    AND TX.CLM_SUBMT_NBR = F.CLM_SUBMT_NBR

-- Join with MS_RPHAI_TPRR for TPRR specific info
LEFT JOIN CORE_RX.CURATED_SCRIPT.MS_RPHAI_TPRR TPRR
    ON TPRR.MESSAGE_ID = F.MESSAGE_ID
    AND TPRR.STORE_NBR = F.STORE_NBR
    AND TPRR.RX_NBR = F.RX_NBR
    AND TPRR.FILL_NBR = F.FILL_NBR

-- Join with PRESCRIPTION_FILL for additional fill details
LEFT JOIN CORE_RX.CURATED_SCRIPT.PRESCRIPTION_FILL PF
    ON PF.STORE_NBR = F.STORE_NBR
    AND PF.RX_NBR = F.RX_NBR
    AND PF.FILL_NBR = F.FILL_NBR
    AND PF.CLAIM_SUBMT_NBR >= F.CLM_SUBMT_NBR
);
