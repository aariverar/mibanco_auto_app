import os

html_features_template = os.path.join(os.getcwd(), "src", "test", "resources", "template_html", "overview-features.html")
html_for_each_feature_template = os.path.join(os.getcwd(), "src", "test", "resources", "template_html", "report-feature.html")
report_folder_path = os.path.join(os.getcwd(), "src", "test", "reports")
template_folder_path = os.path.join(os.getcwd(), "src", "test", "resources", "template_html")
source_files = ["logo_mibanco.png", "main.js", "style.css", "icon.ico"]
source_dir_path = os.getcwd()
source_directories = ["screenshots"]
json_behave_path = os.path.join(os.getcwd(), "json.pretty.output")
json_new_path = os.path.join(os.getcwd(), "New.pretty.output")
word_path1 = os.path.join(os.getcwd(), "Evidencias")



# Variables que se usan para conectarse a Azure portal
account_name = 'storagepruebamibanco' #storage account name
key_vault_name = 'key-db-python-mb' #key vault name
table_name = 'tableExecution' #table name in storage table service
secret_storage_account_key = 'secret-key-mb' #secret name in key vault

account_key='xXR1LBiL62o7OqZzm2ZgK1K7LfvUssSCHwBczIea6XhF8+KkfA1yhts4tTDpJfLbXESKXuyFSj4K+AStE2BqYQ=='