import pyodbc
import get_mssql_data , get_mssql_data1, get_mssql_data2, get_mssql_data3, get_mssql_data4

from datetime import datetime
from mssqlconnect import tempfolder,errorfolder,mig_dir

def insert_pol_mstr(df):    
    pol_head = list(df.columns.values)
    pol_values = list(df.values)
    total_rows = len(df.axes[0])
    total_cols = len(df.axes[1])
    err_str=""
    if total_cols != 2:
             error_str="<b>Invalid Input file, Number of columns expected are 2 given " + str(total_cols) + "<b>"
             f = open(r"error/pol_mstr_errors.txt", "w")
             f.write(error_str) 
             f.close()   
             return      
           
    disp_records = df.head(4)
    error_detail = []
    h = 0
    e = 0
    for j in pol_values:
        f1=open(r"temp/policy_master_proc.txt", "w")
        err_desc = []
        h = h + 1
        f1.write(str(h))
        f1.close()
        if h==1:
             f2=open(r"temp/policy_master_sttime.txt", "w")
             now = datetime.now()
             start_dt= now.strftime("%d/%m/%Y %H:%M:%S")
             
             f2.write(str(start_dt))
             f2.close()
        sql = "INSERT INTO POLICY_MSTR (POLICY_ID,JOIN_DATE) VALUES" + "('" + str(
            j[0]) + "','" + str(j[1]) + "'" + ");"

        print(sql)
        get_mssql_data.insert_data(sql, err_desc)
        if len(err_desc) > 0:
            e = e + 1
            error_detail.append(err_desc)
            err_str=err_str+str(err_desc)+"^^^"

        if (len(pol_values)==h):
            f3=open(r"temp/policy_master_endtime.txt", "w")
            now = datetime.now()
            end_dt= now.strftime("%d/%m/%Y %H:%M:%S")
            f3.write(str(end_dt))
            f3.close()

    f = open(r"error/pol_mstr_errors.txt", "w")
    f.writelines(err_str) 
    f.close()  
def insert_ac_mstr(df):       
    pol_head = list(df.values)
    pol_values = list(df.values)
    total_rows = len(df.axes[0])
    total_cols = len(df.axes[1])
    if total_cols != 3:
        error_line="<b>Invalid Input file, Number of columns expected are 3 given " + str(total_cols) + "<b>^?^"
        f = open(r"error/ac_mstr_errors.txt", "w")
        f.write(error_str) 
        f.close()   
        return      
       
    dest_fields = ['PREM_RECEIVED_A', 'CLAIMS_EXPNS_PAID_A', 'INV_COMPONENT_OUTGO_A', 'ACQ_EXPN_PAID_A',
                   'OTHER_EXPENSES_A', 'INCUR_CLAIMS_NEW_SETTLED', 'INS_FINANCE_INCOME_A']

    error_detail = []
    h = 0
    e = 0
    err_desc=""
    err_str=""
    for j in pol_values:
        f1=open(r"temp/account_master_proc.txt", "w")
        h = h + 1
        f1.write(str(h))
        f1.close()
        if h==1:
             f2=open(r"temp/account_master_sttime.txt", "w")
             now = datetime.now()
             start_dt= now.strftime("%d/%m/%Y %H:%M:%S")
             f2.write(str(start_dt))
             f2.close()
        sql = "SELECT CSFL_KEY FROM CASHFLOW_TYPES WHERE CSFL_TYPE='" + str(j[2]) + "';"
        csfl_data = get_mssql_data1.select_data(sql)
        if len(csfl_data) == 0:
            err_desc = "Invalid Cash Flow Type:" + str(j[2])
            e = e + 1
            error_detail.append(err_desc)
            err_str=err_str+str(err_desc)+"^^^"
        err_desc1 = []
        if len(csfl_data) > 0:
            sql = "INSERT INTO GLCODE_MSTR (GL_CODE,GL_NAME,CSFL_KEY) VALUES" + "('" + str(j[0]) + "','" + str(
                j[1]) + "'," + str(csfl_data[0][0]) + ");"
            print(sql)
            get_mssql_data1.insert_data(sql, err_desc1)
            if len(err_desc1) > 0:
                e = e + 1
                error_detail.append(err_desc1)
                err_str=err_str+str(err_desc1)+"^^^"
        if (len(pol_values)==h):
            f3=open(r"temp/account_master_endtime.txt", "w")
            now = datetime.now()
            end_dt= now.strftime("%d/%m/%Y %H:%M:%S")
            f3.write(str(end_dt))
            f3.close()
        
                
   
    f = open(r"error/ac_mstr_errors.txt", "w")
    f.writelines(err_str) 
    f.close()
    
def insert_prod_mstr(df): 
    pol_head = list(df.values)
    pol_values = list(df.values)
    total_rows = len(df.axes[0])
    total_cols = len(df.axes[1])
    disp_records = df.head()
    headings = df.head()
    if total_cols != 3:
        error_line="<b>Invalid Input file, Number of columns expected are 3 given " + str(total_cols) + "<b>^?^"
        f = open(r"error/prod_mstr_errors.txt", "w")
        f.write(error_line) 
        f.close()   
        return     
        
    base_rider = ['BASE', 'RIDER']
    h = 0
    e=0
    
    error_detail=[]
    err_str=""
    for j in pol_values:
        f1=open(r"temp/product_master_proc.txt", "w")
        err_desc1 = []
        h = h + 1
        f1.write(str(h))
        f1.close()
        if h==1:
             f2=open(r"temp/product_master_sttime.txt", "w")
             now = datetime.now()
             start_dt= now.strftime("%d/%m/%Y %H:%M:%S")
             f2.write(str(start_dt))
             f2.close()
        sql = "INSERT INTO PRODUCT_MSTR (PROD_NAME,PROD_SHRT_NM,BASE_RIDER) VALUES" + "('" + str(
            j[0]) + "','" + str(j[1]) + "','" + str(j[2]) + "')"
        print(sql)
        get_mssql_data2.insert_data(sql, err_desc1)
               
        if len(err_desc1) > 0:
            e = e + 1 
            error_detail.append(err_desc1)
            err_str=err_str+str(err_desc1)+"^^^"

        if (len(pol_values)==h):
            f3=open(r"temp/product_master_endtime.txt", "w")
            now = datetime.now()
            end_dt= now.strftime("%d/%m/%Y %H:%M:%S")
            f3.write(str(end_dt))
            f3.close()
        
    messg_line="<b>Products Upload:Records processed=" + str(h) + "Errors found="  + str(e) + "</b><p> <p><b>Error File can be viewed from Reprots Section</p>"
    f = open(r"error/prod_mstr_errors.txt", "w")
    f.writelines(err_str) 
    f.close()

def insert_pb_mstr(df):
    if 'Policy No' not in df.columns:
        error_line='<b>Invalid File! Please use standard template for Policy Benefits upload</b>("^?^")'
    # Create GOC ID , add a new column to data frame to store goc id
    df['GOC_ID'] = df['Policy No']
    # sort the data frame in policy_no(which is goc_id) order
    df = df.sort_values('GOC_ID', ascending=True)
    # loop thru the goc_id if portfolio_opt='M'
    portfolio_opt='S'
    if portfolio_opt == 'M':

        temp = ''
        for idx, row in df.iterrows():
            if df.loc[idx, 'GOC_ID'] != temp:
                temp = df.loc[idx, 'GOC_ID']
                k = 1
                df.loc[idx, 'GOC_ID'] = str(df.loc[idx, 'GOC_ID']) + str('_00') + str(k)

            else:
                k = k + 1
                df.loc[idx, 'GOC_ID'] = str(df.loc[idx, 'GOC_ID']) + str('_00') + str(k)
    pol_values = list(df.values)
    total_rows = len(df.axes[0])
    total_cols = len(df.axes[1])
    disp_records = df.head(4)
    if total_cols != 4:
        error_line="<b>Invalid Input file, Number of columns expected are 3 given " + str(total_cols) + "<b>^?^"
        f = open(r"error/pb_mstr_errors.txt", "w")
        f.write(error_line) 
        f.close()   
        return     
    dest_fields = ['POLICY_NO', 'BENEFIT']
    error_detail = []
    h = 0
    e = 0
    err_str=""
    for j in pol_values:
        f1=open(r"temp/policy_benefits_proc.txt", "w")
        h = h + 1
        f1.write(str(h))
        f1.close()
        if h==1:
             f2=open(r"temp/policy_benefits_sttime.txt", "w")
             now = datetime.now()
             start_dt= now.strftime("%d/%m/%Y %H:%M:%S")
             f2.write(str(start_dt))
             f2.close()

        sql = "SELECT POLM_KEY FROM POLICY_MSTR WHERE POLICY_ID='" + str(j[0]) + "'"
        #print(sql)
        polm_key = get_mssql_data3.select_data(sql)
        if len(polm_key) == 0:
            err_desc = "Invalid Policy Number:" + str(j[0])
            e = e + 1
            error_detail.append(err_desc)
            err_str=err_str+str(err_desc)+"^^^"

        sql = "SELECT PROD_KEY FROM PRODUCT_MSTR WHERE PROD_SHRT_NM='" + str(j[1]) + "'"
        #print(sql)
        prod_key = get_mssql_data3.select_data(sql)
        if len(prod_key) == 0:
            err_desc = "Invalid Product:" + str(j[1])
            e = e + 1
            error_detail.append(err_desc)
            err_str=err_str+str(err_desc)+"^^^"
        
        err_desc1 = []
        if len(error_detail) == 0:
            sql = "INSERT INTO POL_PROD (POLM_KEY,PROD_KEY,CONTRACT_ID,SUM_ASSURED) VALUES" + "(" + str(
                polm_key[0][0]) + "," + str(prod_key[0][0]) + ",'" + str(j[3]) + "'," + str(j[2]) + ")"
            get_mssql_data3.insert_data(sql, err_desc1)
            if len(err_desc1) > 0:
                e=e+1
            err_str=err_str+str(err_desc1)+"^^^"
        if (len(pol_values)==h):
            f3=open(r"temp/policy_benefits_endtime.txt", "w")
            now = datetime.now()
            end_dt= now.strftime("%d/%m/%Y %H:%M:%S")
            f3.write(str(end_dt))
            f3.close()
        
    #return render_template("error.html", hostname=hostname, error_detail=error_detail, total_records=h,
    #                       error_records=e, process_records=h - e)

    f = open(r"error/pol_ben_errors.txt", "w")
    f.writelines(err_str) 
    f.close()
def insert_port_mstr(df):
    pol_head = list(df.values)
    pol_values = list(df.values)
    total_rows = len(df.axes[0])
    total_cols = len(df.axes[1])
    disp_records = df.head()
    headings = df.head()
    h = 0
    e = 0
    error_detail = []
    err_desc1 = []
    err_str=""
    for j in pol_values:
        f1=open(r"temp/portfolio_master_proc.txt", "w")
        h = h + 1
        f1.write(str(h))
        f1.close()
        if h==1:
             f2=open(r"temp/portfolio_master_sttime.txt", "w")
             now = datetime.now()
             start_dt= now.strftime("%d/%m/%Y %H:%M:%S")
             f2.write(str(start_dt))
             f2.close()
        sql = "SELECT PORT_KEY  FROM  PORTFOLIO_MSTR WHERE PORT_SHRT_NM='" + str(j[1]) + "'"
        #print(sql)
        port_key = get_mssql_data4.select_data(sql)
        if len(port_key) == 0:
            err_desc = "Invalid Portfolio:" + str(j[1])
            e = e + 1
            error_detail.append(err_desc)
            err_str=err_str+str(err_desc)+"^^^"

        else:
            err_desc1 = []
            sql = "UPDATE PRODUCT_MSTR SET PORT_KEY=" + str(port_key[0][0]) + " WHERE PROD_SHRT_NM='" + str(
                j[0]) + "'"
            print(sql)
            get_mssql_data4.insert_data(sql, err_desc1)
    if (len(pol_values)==h):
            f3=open(r"temp/portfolio_master_endtime.txt", "w")
            now = datetime.now()
            end_dt= now.strftime("%d/%m/%Y %H:%M:%S")
            f3.write(str(end_dt))
            f3.close()
        
    messg_line="<b>Portfolio Master Upload:Records processed=" + str(h) + " Errors found=" + str(e) + "</b><p> <p><b>Error File can be viewed from Reprots Section</p>"
    f = open(r"error/portfolio_errors.txt", "w")
    f.writelines(err_str) 
    f.close()  

       