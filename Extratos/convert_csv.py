import pandas as pd
import csv
import glob 
import os
from pathlib import Path
import xlrd
from money import Money


def get_path():
    return str(Path().absolute()) + "/"

def convert_to_csv(output_file_name,my_file, my_sheet_name="Sheet1",my_index=False):
    wb = xlrd.open_workbook(str(my_file), logfile=open(os.devnull, 'w')) # I did this to suppress the Warning msg.
    return pd.read_excel(wb, sheet_name=my_sheet_name, engine='xlrd').to_csv(output_file_name, index=my_index)


def open_csv(csv_file): 
        data = [] 
        with open(csv_file, newline='') as f: 
            reader = csv.reader(f) 
            for k in reader: 
                data.append(k)#list(filter(None,k))) 
        return data

def filter_transactions(raw_datas):
    response = []
    seen = []
    for data in raw_datas: 
        # data[1][22]--> header
        # End of Transaction Cell --> "Saldo atual"     

        last = 0
        for row in data[1:]:
            for j, content in enumerate(row[:]):
                # Find End of Transactions:
                if content[2] == "Saldo atual": # Next thing after transactions ends.
                    # ToDo: Create the test for this: total # rows - position of 'Saldo atual'  = 33.
                    # test.assert(len(row)-j,33)
                    # print(j, len(row), " = ", len(row)- j)
                    # input()
                    last = j
        transactions = data[1][22:last]
        if transactions not in seen:
            response.append([data[0],transactions])
            seen.append(transactions)
    return response

def list_excel(path = get_path()):
    return glob.glob(path + "/*.xls*")

def list_csv(path = get_path()):
    return glob.glob(path + "/*.csv")

def exists(filepath):
    if os.path.exists(filepath):
        print(filepath, 'exists.')
        return True

def convert_all(input_folder, output_folder):
    excel_files = list_excel(input_folder)
    for excel_file in excel_files:
        filepath = "{0}{1}.csv".format(output_folder,excel_file[len(input_folder):-4]) # without .xls
        if not exists(filepath):
            convert_to_csv(filepath, excel_file)

def consolidate_reports(consolidated_data, folder_name):
    data = []
#     seen = []
    datas = []
    csv_files = list_csv(get_path() + folder_name)
    for csv_file in csv_files:
        data = open_csv(csv_file)
        for row in data:
        #     if row not in seen:
                datas.append(row)
                # seen.append(row)
    return datas


# return a list of lists :/
# raw_data = [[report], [report], [report]]
def consolidate_data(folder_name):
    data = []
    raw_datas = []
    csv_files = list_csv(get_path() + folder_name)
    for csv_file in csv_files:
        data = open_csv(csv_file)
        raw_datas.append([csv_file[len(get_path()):], data])
    # print(raw_datas[0])
    # input()
    return raw_datas

def save_single_report(output_file, reports):
    # reports = [[filname, report1], [filename, report2], [...]]
    # reportN = [[headers],[transaction1], [transaction2], [transactionN...]]

    # print(reports)
    # input()
    row_headers = reports[2][1][0]
    headers =[]
    headers.append("Filename")
    
    for header in row_headers:
        if header:
            headers.append(header)# =[header for header in row_headers if header]
    # print(headers)
    # input()
    positions = []
    for i, header in enumerate(row_headers):
        positions.append(i) if header else None 
    # print(headers)
    # print(positions)
    # input()
    f = csv.writer(open(output_file, "w", encoding="mac-roman"))
    f.writerow(headers)
    # print(reports[0][0])
    # input()
    response = []
    # response.append(headers)
    data = {} 
    for transactions in reports:
        # check if transactions[1][0] == headers
        for position in positions:
            if transactions[1][0][position] not in headers:
                print(transactions[0][position])
                input("Dados Diferente?")
        for i, transaction in enumerate(transactions[1][1:]): # header not needed.
                datas = []
                datas.append(transactions[0][:])
                
                for pos, header in enumerate(headers[1:]):
                    data[header] = transaction[positions[pos]]
                    try: 
                        # todo
                        data[header] = Money(data[header], "BRL")
                    except:
                        None
                    datas.append(data[header]) #.replace(".",",")
                    # if data[header] == '30000': 
                    #     print(datas)
                    #     input()
                if not all(value is '' for value in datas[1:]):
                    response.append(datas)
                    f.writerow(datas)
    df = pd.DataFrame(response, columns=headers)
    return df

def replace_decimal_notation(raw_datas):
    # raw_datas = [[report1], [report2], [report...]] 
    # # report1 = [transacton1, transaction2]
        for report in raw_datas:
                for transaction in report:
                    for field in transaction:
                        field = field.replace(".", ",")
        # datas = [field.replace(".",",") for field in transaction for transaction in report for report in datas]
        return report


def outputs_to(folder_name) -> str:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name


    

def main(output_report='statements.csv', csv_folder_name='reports_csv', excel_folder_name='reports_xls'):
    print("##### Converting all Excels to CSV")
    convert_all(excel_folder_name, outputs_to(csv_folder_name))
    print("##### Consolidating datas") # list with every report.
    # raw_datas will be [[report1], [report2], [report...] ]
    raw_datas = consolidate_data(csv_folder_name)
#     print("##### Consolidating reports")
#     datas = consolidate_reports(raw_datas, csv_folder_name)
    print("##### Filtering Transactions")
    # datas_mov will be [[transactions_from_report1], [transactions_from_report2], [...]]
    datas_mov = filter_transactions(raw_datas)
    # print("##### Replacing decimal notation '.' -> ','")
    # datas_mov = replace_decimal_notation(datas_mov)
    print("##### Saving in a single Report")
    # response = []
    response = save_single_report(output_report, datas_mov)
    return [raw_datas, datas_mov, response]

if __name__ == '__main__':
    raw_data, datas_mov, df = main(output_report='statements.csv', csv_folder_name='reports_csv', excel_folder_name='reports_xls')