
```sql
SELECT 
    -- Claim Identification
    MESSAGE_ID,                  -- Unique identifier for the TPRR message/event
    STORE_NBR,                  -- Store number where transaction occurred
    RX_NBR,                     -- Prescription number
    FILL_NBR,                   -- Fill number of the prescription
    CLM_SUBMT_NBR,             -- Claim submission attempt number
    
    -- Patient Information
    CVS_CENTR_PAT_NBR,         -- Centralized patient identifier
    CLM_DT,                    -- Date of the claim
    
    -- Transaction Status
    TXN_RSP_STAT_CD,          -- Transaction response status code (P=Paid, R=Rejected)
    REJECT_CD_1,              -- Primary rejection code from insurance
    REJECT_CD_2,              -- Secondary rejection code
    REJECT_CD_3,              -- Third rejection code
    REJECT_CD_4,              -- Fourth rejection code 
    REJECT_CD_5,              -- Fifth rejection code
    CONCAT_MSG_TXT,           -- Concatenated message text from response
    
    -- Cost Information
    RQST_PRC_INGRD_SUBM_COST_AMT,  -- Submitted ingredient cost amount
    RQST_CLM_DISPNG_QTY,           -- Requested dispensing quantity
    RQST_CLM_DAYS_SUPPLY_QTY,      -- Requested days supply
    SPLIT_BILL_CD,                  -- Split billing indicator
    BIN_NBR,                        -- Bank Identification Number for insurance
    
    -- Insurance Information
    RQST_INS_RSPMBR_ID,            -- Insurance member ID
    RQST_INS_GROUP_ID,             -- Insurance group ID
    RQST_CLM_PROD_SVC_QUAL_CD,     -- Product/service qualifier code
    RQST_PRC_UC_PRC_AMT,           -- Usual and customary price amount
    
    -- Eligibility Flag
    ELIGIBILITY_YN,                 -- Flag indicating if rejection is eligibility-related
    
    -- Plan Information  
    CONDOR_PLAN_NBR,                -- Internal plan identifier
    AGENCY_TYPE_CD,                 -- Type of insurance agency code
    AGENCY_TYPE_DSC,                -- Description of insurance agency type
    COORDINATION_OF_BENEFITS_AGENCY_TYPE_CD,    -- COB agency type code
    COORDINATION_OF_BENEFITS_AGENCY_TYPE_DSC,   -- COB agency type description

    -- Target Variable
    NBA5_ATTEMPTED,                 -- Whether edit to cash was attempted (target variable)

    -- TPRR Information
    NBA_CD,                         -- Next Best Action code
    AUTOMATION_LEVEL_CD,            -- Level of automation applied
    NON_PREFERRED_IND,             -- Non-preferred product indicator
    RTS_ELIGIBLE_IND,              -- Return to stock eligibility
    AUTOMATION_COMMENT_TXT,         -- Automation comment
    FILL_NOTES_TXT,                -- Fill notes
    CONFIDENCE_SCORE,              -- Confidence score of the decision
    PAYER_MSG,                     -- Message from the payer

    -- Prescription Fill Details
    NDC,                           -- National Drug Code
    INTENDED_DISPENSE_QTY,         -- Originally intended dispense quantity
    INTENDED_DAYS_SUPPLY_QTY,      -- Originally intended days supply
    PATIENT_AGE_NBR,               -- Patient's age
    FILL_STATUS_CD,                -- Status of the fill
    FILL_STATE_CD,                 -- State of the fill
    FILL_TYP_CD,                   -- Type of fill
    REMAINING_QTY,                 -- Remaining quantity
    VERIFIED_TS,                   -- Verification timestamp
    PICKUP_TS,                     -- Pickup timestamp
    DISPENSE_TS,                   -- Dispensing timestamp
    RX_ORIGIN_CD,                  -- Prescription origin code
    EXPEDITE_IND,                  -- Expedited indicator
    CENTRAL_FILL_IND,              -- Central fill indicator
    QTY_DIFF,                      -- Difference between intended and actual quantity
    DAYS_DIFF,                     -- Difference between intended and actual days supply

    -- Drug Information
    GCN_SEQUENCE_NBR,              -- Generic Code Number sequence
    HICS_CD,                       -- Hierarchical Ingredient Code System
    DEA_CD,                        -- Drug Enforcement Administration code
    THERAPEUTIC_CLASS_CD,          -- Therapeutic class code
    GENERIC_IND,                   -- Generic drug indicator
    CVS_MAINTAIN_IND,              -- CVS maintenance indicator
    PACKAGE_SIZE_AMT,              -- Package size amount
    UNIT_DOSE_IND,                 -- Unit dose indicator
    AMP_UNIT_AMT,                  -- Average Manufacturer Price per unit
    MAC_UNIT_PRC_AMT,              -- Maximum Allowable Cost per unit
    CALCULATE_UNIT_COST_AMT,       -- Calculated unit cost

-- Drug Historical Metrics (GCN Level)
    DRUG_CDC_RATE,               -- Rate of CDC (Central Drug Control) utilization for this drug
    TIMES_CDC_COUNT,             -- Count of CDC transactions for this drug
    DRUG_COUPON_RATE,           -- Rate of coupon usage for this drug
    DRUG_COUPON_COUNT,          -- Count of coupon transactions for this drug
    DRUG_CASH_RATE,             -- Rate of cash transactions for this drug
    DRUG_CASH_COUNT,            -- Count of cash transactions for this drug
    DRUG_RTS_RATE,              -- Rate of return to stock for this drug
    DRUG_TOTAL_PAID,            -- Total paid transactions for this drug
    DRUG_TOTAL_SOLD,            -- Total sold quantity for this drug

    -- Drug Historical Metrics (HICS Level - Therapeutic Class)
    CLASS_CDC_RATE,             -- Rate of CDC utilization for this drug class
    CLASS_CDC_COUNT,            -- Count of CDC transactions for this drug class
    CLASS_COUPON_RATE,          -- Rate of coupon usage for this drug class
    CLASS_CASH_RATE,            -- Rate of cash transactions for this drug class
    CLASS_CASH_COUNT,           -- Count of cash transactions for this drug class
    CLASS_RTS_RATE,             -- Rate of return to stock for this drug class
    CLASS_TOTAL_PAID,           -- Total paid transactions for this drug class
    CLASS_TOTAL_SOLD,           -- Total sold quantity for this drug class
    DRUG_HIST_SEQ_NO,           -- Sequence number for drug history record

    -- Patient Geographic Information
    PATIENT_LATITUDE,           -- Patient's location latitude
    PATIENT_LONGITUDE,          -- Patient's location longitude

    -- Patient History (NDE - New Drug Event)
    NEW_PATIENT_FLAG,           -- Flag indicating if patient is new (within 730 days)
    CASH_DISCOUNT_SCRIPTS_90D,  -- Number of cash discount scripts in last 90 days
    CASH_SCRIPTS_90D,           -- Number of cash scripts in last 90 days
    TOTAL_SCRIPTS_90D,          -- Total number of scripts in last 90 days
    SAME_CREDIT_CARD_COUNT_90D, -- Count of transactions with same credit card in 90 days

    -- Patient History (180-day)
    PATIENT_CASH_RATE,         -- Rate of cash payments by patient
    PATIENT_TOTAL_PAID,        -- Total paid transactions by patient
    PATIENT_AVG_PAY_180D,      -- Average payment amount in last 180 days
    PATIENT_MEDIAN_PAY_180D,   -- Median payment amount in last 180 days
    PATIENT_MAX_PAY_180D,      -- Maximum payment amount in last 180 days
    PATIENT_DENIAL_COUNT_180D, -- Count of denials in last 180 days

    -- Patient GCN History
    GCN_MAX_DAYS_SUPPLY,       -- Maximum days supply for patient's GCN history
    GCN_MIN_DAYS_SUPPLY,       -- Minimum days supply for patient's GCN history
    PATIENT_DRUG_CASH_RATE,    -- Patient's cash payment rate for this drug
    PATIENT_DRUG_TOTAL_PAID,   -- Patient's total paid for this drug
    PATIENT_DRUG_SOLD_COUNT,   -- Count of this drug sold to patient

    -- Additional Patient Demographics
    RQST_PAT_GENDER_ID,        -- Patient's gender identifier
    RQST_PAT_ZIP_CD,           -- Patient's ZIP code

    -- Prescriber Information
    PCP_PRESCBR_NBR,           -- Primary care provider number
    CVS_CENTR_PSCBR_NBR,       -- Centralized prescriber number
    RQST_PRESCBR_QUAL_ID,      -- Prescriber qualifier ID (NPI)

    -- Additional Claim Details
    RQST_CLM_PROD_SVC_ID,      -- Product/service identifier
    RQST_CLM_DAW_CD,           -- Dispense as Written code
    RQST_CLM_RX_WRITTEN_DT,    -- Date prescription was written
    RQST_CLM_ALLOW_REFILL_QTY, -- Number of refills allowed

    -- Plan Details
    AGENCY_NM,                 -- Insurance agency name
    CONDOR_PLAN_NM,           -- Condor plan name

    -- Timestamps
    CLM_DT_TME,               -- Claim date and time
    RECORD_CREATE_TS          -- Record creation timestamp
---------------------------------------
--Omitted
-- From CORE_RX.CURATED_PRODUCT.DRUG
SELECT
    LABEL_NM,            -- Full drug name/label, provides context about drug type
    GNN_CD,              -- Generic name, useful for drug classification
    STRENGTH_CD,         -- Drug strength, important for cost/coverage analysis
    CLASS_CD,            -- Drug class code, additional therapeutic classification
    TOP_SELLER_IND,      -- Indicates popular medications
    DRUG_RANK_NBR,       -- Popularity ranking, could indicate likelihood of coverage
    EXPIRE_DAYS_NBR;     -- Days until expiration, might affect cash conversion

-- From APP_RPHAI.CURATED_RPHAI.PATIENTCARD_JSON_HIST
SELECT
    -- 30-day history provides recent trends
    PARSE_JSON(REQUEST_JSON):history.history30d.avgPrntPayAmmt::float AS AVG_PAY_30D,
    PARSE_JSON(REQUEST_JSON):history.history30d.prctTimesCdc::float AS CDC_RATE_30D,
    PARSE_JSON(REQUEST_JSON):history.history30d.totalTimesPaid::int AS TOTAL_PAID_30D,

    -- HIC3 class history shows therapeutic class patterns
    PARSE_JSON(REQUEST_JSON):history.hic3180d.prctTimesPaidCash::float AS HIC3_CASH_RATE,
    PARSE_JSON(REQUEST_JSON):history.hic3180d.noOfAttempts::int AS HIC3_ATTEMPTS,
    PARSE_JSON(REQUEST_JSON):history.hic3180d.denialCount::int AS HIC3_DENIALS;

-- From CORE_RX.CURATED_NCPDP.FACT_NCPDP_ADJ_TXN
SELECT
    REFIL_TOO_SOON_ACTIV,       -- Indicates if refill timing is an issue
    AUTO_RETRY_IND,             -- Shows if claim was automatically retried
    RQST_CLM_PRIOR_AUTH_CD,     -- Prior authorization status
    RQST_CLM_OTHER_COV_CD,      -- Other insurance coverage indicator
    RQST_PRC_DISPNG_FEE_SUBM_AMT,  -- Dispensing fee, affects total cost
    RQST_PRC_GROSS_DUE_AMT;     -- Total amount due, key for cash conversion decision

-- From CORE_RX.CURATED_SCRIPT.MS_RPHAI_TPRR
SELECT
    LOGGING_LIST:model_input.preferred_products::variant as PREFERRED_PRODUCTS,  -- Alternative products
    LOGGING_LIST:rel_codes::variant as REJECTION_CODES,  -- Detailed rejection codes
    LOGGING_LIST:msg_in_resp::string as MESSAGE_IN_RESPONSE;  -- Additional response details

-- From CORE_RX.CURATED_SCRIPT.PRESCRIPTION_FILL
SELECT
    PATIENT_COUNSEL_CD,         -- Patient counseling status
    PHONE_NOTIFICATION_IND,     -- Contact preference
    PROMISE_DT_CD,             -- Promise date code
    SOURCE_CD,                 -- Source of prescription
    COMPOUND_IND;              -- Whether prescription is compound medication
