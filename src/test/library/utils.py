import json
import os
import shutil
from datetime import datetime
from jinja2 import Template
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def generate_html_for_all_features(template, output_path, data, scenarios, steps, scenarios_information):

    with open(template, 'r', encoding='utf-8') as file:
        template_content = file.read()
    template = Template(template_content)

    # Formatear la fecha y hora según el formato especificado
    execution_time = datetime.now()
    formato = "%d %b %Y, %H:%M"
    fecha_formateada = execution_time.strftime(formato)

    total_features = len(data)
    total_duration, average_duration = sum_durations_and_average_duration(data)

    html_output = template.render(features=data, 
                                  total_features=total_features, 
                                  total_scenarios=scenarios, 
                                  total_steps=steps, 
                                  scenarios_information=scenarios_information,
                                  date=fecha_formateada,
                                  total_duration=total_duration,
                                  average_duration=average_duration)
    
    # Write the HTML output to a file
    output_path = os.path.join(output_path,"overview-features.html")
   
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_output)

def generate_html_for_each_feature(template, output_path, data):

    with open(template, 'r', encoding='utf-8') as file:
        template_content = file.read()
    template = Template(template_content)

    # Formatear la fecha y hora según el formato especificado
    execution_time = datetime.now()
    formato = "%d %b %Y, %H:%M"
    fecha_formateada = execution_time.strftime(formato)

    for index, feature in enumerate(data):

        html_output = template.render(feature=feature,
                                      feature_index=index, 
                                      date=fecha_formateada)
        
        # Añadir el índice al nombre del archivo
        output_file = os.path.join(output_path, f"report-feature-{index+1}.html")

        # Write the HTML output to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_output)

def process_data_json(data_json_path):

    with open(data_json_path, 'r') as file:
        test_results = json.load(file)

    data = []
    for feature in test_results:
        feature_name = feature['name']
        scenarios = []
        scenario_passed_count = 0
        scenario_failed_count = 0
        scenario_skipped_count = 0
        step_passed_count = 0
        step_failed_count = 0
        step_skipped_count = 0

        for scenario in feature['elements']:
            scenario_name = scenario['name']
            status = scenario['status']
            steps = []

            if status == "passed":
                scenario_passed_count += 1
            elif status == "failed":
                scenario_failed_count += 1
            else:
                scenario_skipped_count += 1
            
            for step in scenario['steps']:
                step_name = step['name']
                step_keyword = step['keyword']

                if 'result' in step:
                    step_status = step['result'].get('status', 'unknown') 
                    step_message = step['result'].get('message', '')
                    step_time = step['result'].get('duration', 0)
                    step_img = step['result'].get('imagen', [])
                else:
                    step_status = 'failed'
                    step_message = 'failed'
                    step_time = 0
                    step_img = []
                
                if status == 'skipped': # Si el escenario es skipped, los steps también
                    step_status = 'skipped'
                    step_message = 'skipped'
                    step_time = 0
                    step_img = []
                
                if step_status == "passed":
                    step_passed_count += 1
                elif step_status == "failed":
                    step_failed_count += 1
                else:
                    step_skipped_count += 1

                steps.append({'name': step_name,
                              'keyword': step_keyword, 
                              'status': step_status,
                              'message': step_message,
                              'duration': step_time,
                              'images': step_img})
                
            scenarios.append({'name': scenario_name, 
                              'status': status, 
                              'steps': steps})
            
        data.append({'feature_name': feature_name, 
                     'scenarios': scenarios,
                     'scenario_passed_count': scenario_passed_count,
                     'scenario_failed_count': scenario_failed_count,
                     'scenario_skipped_count': scenario_skipped_count,
                     'step_passed_count': step_passed_count, 
                     'step_failed_count': step_failed_count,
                     'step_skipped_count': step_skipped_count,
                     'scenarios_total': scenario_passed_count + scenario_failed_count + scenario_skipped_count,
                     'steps_total': step_passed_count + step_failed_count + step_skipped_count})
    return data

def count_total_scenarios_and_steps(data):
    total_scenarios = 0
    total_steps = 0
    total_scenarios_passed = 0
    total_scenarios_failed = 0
    total_scenarios_skipped = 0

    for feature in data:
        total_scenarios += feature['scenarios_total']
        total_steps += feature['steps_total']
        total_scenarios_passed += feature['scenario_passed_count']
        total_scenarios_failed += feature['scenario_failed_count']
        total_scenarios_skipped += feature['scenario_skipped_count']

    scenarios_information = {'total_scenarios_passed': total_scenarios_passed,
    'total_scenarios_failed': total_scenarios_failed,
    'total_scenarios_skipped': total_scenarios_skipped}
    
    return total_scenarios, total_steps, scenarios_information

def create_report_folder(template_folder_path, report_folder_path, source_files, source_directories, source_dir_path, word_path):
    date = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
    folder_name = f"report-{date}"

    html_features_output = os.path.join(report_folder_path, folder_name)
    os.makedirs(html_features_output, exist_ok=True)

    # Copiar los archivos
    for file_name in source_files:
        source_file_path = os.path.join(template_folder_path, file_name)
        destination_file_path = os.path.join(html_features_output, file_name)
        shutil.copy(source_file_path, destination_file_path)
    
    # Copiar los directorios
    for dir_name in source_directories:
        source_dir_path = os.path.join(source_dir_path, dir_name)
        destination_dir_path = os.path.join(html_features_output, dir_name)
        shutil.copytree(source_dir_path, destination_dir_path)
    
    destination_evidences_path = os.path.join(html_features_output, "Evidencias")
    shutil.copytree(word_path, destination_evidences_path)

    return html_features_output

def sum_durations_and_average_duration(data):
    total_duration = 0
    scenario_count = 0
    for feature in data:
        for scenario in feature['scenarios']:
            if scenario['status'] != 'skipped':
                for step in scenario['steps']:
                    total_duration += step['duration']
                scenario_count += 1 # ignore scenario skipped
    if scenario_count == 0:
        return "0s", "0s"
    
    average_duration = total_duration / scenario_count
    total_duration_str = str(round(total_duration, 2)) + "s"
    average_duration_str = str(round(average_duration, 2)) + "s"

    return total_duration_str, average_duration_str

def delete_screenshots_folder(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        shutil.rmtree(folder_path)

def modify_json_with_img(json_data,step_img,escenario_new_name):
    for feature in json_data:
        for element in feature.get('elements', []):
            for step in element.get('steps', []):
                for img in step_img:
                    if img['step_name'] == step['name'] and img['scenario_name'] == element['name']:
                        step['result']['imagen'] = img['imagen']
                        break
            for names in escenario_new_name:
                if element['name']==names['scenario_name']:
                    element ['name']=names['scenario_new_name']
    return json_data

def modify_json_behave(step_img, json_behave_path, json_new_path,escenario_new_names):
    with open(json_behave_path,'a') as json_file:
        json_file.write("]")
    
    with open(json_behave_path, 'r') as file:
        data = json.load(file)
    
    modified_data = modify_json_with_img(data, step_img, escenario_new_names)

    with open(json_new_path, 'w') as file:
        json.dump(modified_data,file,indent=4)

def json_to_junit(json_input, xml_output):
    with open(json_input, 'r') as json_file:
        data = json.load(json_file)

    testsuites = Element('testsuites')
    for feature in data:
        testsuite = SubElement(testsuites, 'testsuite', name=feature['name'], tests=str(len(feature['elements'])))
        for scenario in feature['elements']:
            total_duration = 0
            if scenario['status'] != 'skipped':
                # Calcular la duración total de los pasos del escenario solo si no está skipped
                for step in scenario['steps']:
                    if 'result' in step and step['result']['status'] != 'skipped':
                        total_duration += step['result']['duration']
            testcase = SubElement(testsuite, 'testcase', classname=feature['name'], name=scenario['name'], time=str(total_duration))
            if scenario['status'] == 'skipped':
                skipped = SubElement(testcase, 'skipped')
                skipped.text = "Scenario skipped"
            elif scenario['status'] != 'passed':
                failure = SubElement(testcase, 'failure', message="Test failed")
                failure.text = scenario['name']
            for step in scenario['steps']:
                if scenario['status'] == 'skipped' or ('result' in step and step['result']['status'] == 'skipped'):
                    if not 'skipped' in testcase.attrib:
                        skipped = SubElement(testcase, 'skipped')
                        skipped.text = "Step skipped"
                elif 'result' in step and step['result']['status'] != 'passed':
                    failure = SubElement(testcase, 'failure', message="Step failed")
                    failure.text = step['name']

    raw_xml = tostring(testsuites, 'utf-8')
    pretty_xml = parseString(raw_xml).toprettyxml(indent="  ")

    with open(xml_output, 'w') as xml_file:
        xml_file.write(pretty_xml)