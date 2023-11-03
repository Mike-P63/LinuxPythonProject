import subprocess

if __name__ == "__main__":
    def check_output(command, text):
        try:
            output = subprocess.check_output(command, shell=True).decode()
            if text in output:
                return True
            else:
                return False
        except subprocess.CalledProcessError:
            return False

print(check_output("rm --help", "force"))
print(check_output("rm --help", "Dorce"))