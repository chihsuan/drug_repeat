 \copy drug_name FROM 'lib/drug_name_list.csv' DELIMITER ',' CSV;

create table oo2012_tmp  as  select * from  oo2012  where  DRUG_NO  in (select DRUG_NO  from drug_name);

create table oocd_tmp as select aa.*,bb.FUNC_DATE,bb.ID_BIRTHDAY,bb.ID,bb.CARD_SEQ_NO,bb.PART_NO,bb.ACODE_ICD9_1,bb.ACODE_ICD9_2,bb.ACODE_ICD9_3,bb.DRUG_DAY,bb.PRSN_ID,bb.ID_SEX
from oo2012 as aa left join cd2012 as bb on (aa.FEE_YM=bb.FEE_YM and aa.APPL_TYPE=bb.APPL_TYPE and aa.APPL_DATE=bb.APPL_DATE and aa.CASE_TYPE=bb.CASE_TYPE and
        aa.SEQ_NO=bb.SEQ_NO and aa.HOSP_ID=bb.HOSP_ID);

\copy (select id,drug_no,case_type,drug_fre,drug_use,func_date,drug_day from oocd_tmp) to 'hyper_drug.csv' with CSV;
