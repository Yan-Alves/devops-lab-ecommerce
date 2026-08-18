import subprocess
from datetime import datetime
import sys

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True)
    except subprocess.CalledProcessError as err:
        print(f"Erro ao executar o comando: {cmd}\nDetalhe: {err}")
        sys.exit(1)

def main():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"--- Auditoria de Cluster Kubernetes | {agora} ---")
    
    print("\n[+] Verificando status dos Nodes...")
    nodes = run_command("kubectl get nodes -o wide")
    print(nodes)
    
    print("[+] Listando todos os Pods (All Namespaces)...")
    pods = run_command("kubectl get pods -A")
    print(pods)
    
    print("--- Auditoria finalizada! Tudo rodando da maneira correta. ---")

if __name__ == "__main__":
    main()
