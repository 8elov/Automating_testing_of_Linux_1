import subprocess


def execute_and_check_output(linux_command: str, text):
    try:
        result = subprocess.check_output(linux_command, shell=True, text=True)

        return text in result

    except subprocess.CalledProcessError:
        return False


linux_command = "echo 'Hello, World!'"
text = "Hello"
print(execute_and_check_output(linux_command, text))
