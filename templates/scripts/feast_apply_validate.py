import os
import subprocess

def run_feast_command(cmd):
    print(f"Executando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise Exception(f"Erro ao executar: {cmd}")

if __name__ == "__main__":
    os.chdir("templates/feature_repo")

    run_feast_command("feast apply")
    run_feast_command("feast validate")

    print("✅ Feast apply e validate concluídos.")