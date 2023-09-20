import subprocess
import time
import argparse

def test_program(program_path, input_data, expected_output):
    # Definisci l'input del programma (se necessario)
    
    # Avvia il timer
    start_time = time.time()

    try:
        # Esegui il programma esterno utilizzando subprocess
        process = subprocess.Popen(["python", program_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Invia input (se necessario)
        stdout, stderr = process.communicate(input=input_data)

        # Calcola il tempo di esecuzione
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Output: {stdout.strip()}")
        
        # Verifica l'output
        success = True
        if stdout.strip() != expected_output:
            print("Test failed! Output mismatch.")
            success = False

        if success:
            print(f"Test passed! Execution time: {execution_time} seconds")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-p", "--path_to_program",
                        type = str, help = "path to the program to execute"
                       )
    
    parser.add_argument("-e", "--expected_output_file",
                        type = str, help = "file with data to check the program"
                       )
    
    parser.add_argument("-i", "--input_data_file", default=None,
                        type = str, help = "file with data to input to the program"
                       )
    
    args = parser.parse_args()
    
    program_to_test = args.path_to_program
    input_data_file = args.input_data_file
    expected_output_file = args.expected_output_file

    with open(input_data_file) as f:
        lines = f.read().splitlines()

    input_data = ''
    for i, line in enumerate(lines):
        input_data += str(line)
        if i+1 != len(lines) :
            input_data += ", "
            
    print(f"Input: {input_data}")
    
    with open(expected_output_file) as f:
        output_lines = f.read().splitlines()
        
    expected_output = ''
    for i, line in enumerate(output_lines):
        expected_output += str(line)
        if i+1 != len(output_lines) :
            expected_output += ", "
        
    print(f"Expected output: {expected_output}")
    
    test_program(program_to_test, input_data, expected_output)