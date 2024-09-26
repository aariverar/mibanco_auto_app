import os
from utils import *
from variables import *

# Generate the HTML report
data_json_path= os.path.join(os.getcwd(), "New.pretty.output")
data = process_data_json(data_json_path)
total_scenarios, total_steps, scenarios_information= count_total_scenarios_and_steps(data)
report_folder = create_report_folder(template_folder_path, report_folder_path, source_files, source_directories, source_dir_path)

delete_screenshots_folder(source_directories)

generate_html_for_all_features(html_features_template, report_folder, data, total_scenarios, total_steps, scenarios_information)
generate_html_for_each_feature(html_for_each_feature_template, report_folder, data)
json_to_junit('json.pretty.output', 'output.xml')