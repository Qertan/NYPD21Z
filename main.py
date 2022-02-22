import pit_package.pit_poland
katalog="Z:/Kuba/Studia/uw/III rok/nypd"
gminy_pit_path20=katalog + "/pit_2020/20210215_Gminy_2_za_2020.xlsx"
powiaty_NPP_pit_path20=katalog + "/pit_2020/20210215_Miasta_NPP_2_za_2020.xlsx"
powiaty_pit_path20=katalog + "/pit_2020/20210211_Powiaty_za_2020.xlsx"
wojewodztwa_pit_path20=katalog + "/pit_2020/20210211_Województwa_za_2020.xlsx"

gminy_ppl_path20=katalog +"/ludnosc/Tabela_IV.xls"
powiaty_ppl_path20=katalog +"/ludnosc/Tabela_III.xls"
wojewodztwa_ppl_path20=katalog +"/ludnosc/Tabela_II.xls"

gminy_pit_path19=katalog+"/pit_2019/20200214_Gminy_za_2019.xlsx"
powiaty_NPP_pit_path19=katalog+"/pit_2019/20200214_Miasta_NPP_za_2019.xlsx"
powiaty_pit_path19=katalog+"/pit_2019/20200214_Powiaty_za_2019.xlsx"
wojewodztwa_pit_path19=katalog+"/pit_2019/20200214_Wojewodztwa_za_2019.xlsx"

data_gminy_pit_20=pit_package.pit_poland.data_import.gminy_import_pit(gminy_pit_path20)
data_powiaty_pit_20=pit_package.pit_poland.data_import.powiaty_import_pit(powiaty_pit_path20, powiaty_NPP_pit_path20)
data_wojewodztwa_pit_20=pit_package.pit_poland.data_import.wojewodztwa_import_pit(wojewodztwa_pit_path20)

data_gminy_ppl_20=pit_package.pit_poland.data_import.gminy_import_ppl(gminy_ppl_path20)
data_powiaty_ppl_20=pit_package.pit_poland.data_import.powiaty_import_ppl(powiaty_ppl_path20)
data_wojewodztwa_ppl_20=pit_package.pit_poland.data_import.wojewodztwa_import_ppl(wojewodztwa_ppl_path20)

data_gminy_pit_19=pit_package.pit_poland.data_import.gminy_import_pit(gminy_pit_path19)
data_powiaty_pit_19=pit_package.pit_poland.data_import.powiaty_import_pit(powiaty_pit_path19, powiaty_NPP_pit_path19)
data_wojewodztwa_pit_19=pit_package.pit_poland.data_import.wojewodztwa_import_pit(wojewodztwa_pit_path19)

diff_gminy = pit_package.pit_poland.analysis.difference_pit(data_gminy_pit_19, data_gminy_pit_20)
diff_powiaty = pit_package.pit_poland.analysis.difference_pit(data_powiaty_pit_19, data_powiaty_pit_20)
diff_wojewodztwa = pit_package.pit_poland.analysis.difference_pit(data_wojewodztwa_pit_19, data_wojewodztwa_pit_20)

avg_gminy=pit_package.pit_poland.analysis.average_income(data_gminy_pit_20, data_gminy_ppl_20)
avg_powiaty=pit_package.pit_poland.analysis.average_income(data_powiaty_pit_20, data_powiaty_ppl_20)
avg_wojewodztwa=pit_package.pit_poland.analysis.average_income(data_wojewodztwa_pit_20, data_wojewodztwa_ppl_20)
#avg_gminy.to_excel(excel_writer=katalog+"/avg_gminy.xlsx", engine="openpyxl")
#avg_powiaty.to_excel(excel_writer=katalog+"/avg_powiaty.xlsx", engine="openpyxl")
#avg_wojewodztwa.to_excel(excel_writer=katalog+"/avg_wojewodztwa.xlsx", engine="openpyxl")

weigh_avg_powiaty=pit_package.pit_poland.analysis.weighted_average(avg_gminy, avg_powiaty)
weigh_avg_wojewodztwa=pit_package.pit_poland.analysis.weighted_average(avg_powiaty, avg_wojewodztwa)
#weigh_avg_powiaty.to_excel(excel_writer=katalog+"/weigh_avg_powiaty.xlsx", engine="openpyxl")
#weigh_avg_wojewodztwa.to_excel(excel_writer=katalog+"/weigh_avg_wojewodztwa.xlsx", engine="openpyxl")

var_powiaty = pit_package.pit_poland.analysis.variance_income(avg_gminy, avg_powiaty)
var_wojewodztwa = pit_package.pit_poland.analysis.variance_income(avg_powiaty, avg_wojewodztwa)
#pit_package.pit_poland.data_export.save_to_excel(var_wojewodztwa, katalog, "var_wojewodztwa")
#var_powiaty.to_excel(excel_writer = katalog+"/var_powiaty.xlsx", engine="openpyxl")
#var_wojewodztwa.to_excel(excel_writer = katalog+"/var_wojewodztwa.xlsx", engine="openpyxl")

#pit_package.pit_poland.analysis.charts.diff_pie(diff_wojewodztwa, "Różnice w województwach")
pit_package.pit_poland.analysis.charts.avg_bar(avg_wojewodztwa, "Ranking dochdoów w województwach")

powiaty_all = weigh_avg_powiaty.join()