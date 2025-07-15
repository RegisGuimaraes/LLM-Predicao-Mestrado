
import os
import subprocess

files_to_compress = [
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2024/itr_cia_aberta_BPP_ind_2024.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2022/itr_cia_aberta_BPP_con_2022.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-17.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-15.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-7.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2024/itr_cia_aberta_DMPL_con_2024.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-18.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-19.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2024/itr_cia_aberta_DMPL_ind_2024.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-14.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-5.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2022/itr_cia_aberta_DMPL_ind_2022.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-13.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-20.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2023/itr_cia_aberta_DMPL_ind_2023.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2022/itr_cia_aberta_DMPL_con_2022.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Baixados CVM/itr_cia_aberta_2023/itr_cia_aberta_DMPL_con_2023.csv",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-16.txt",
    "/home/ubuntu/Codigos/Mestrado_Github/Arquivos Previsoes/Previsoes/prompts_o3-mini-high-IBRX100-8.txt"
]

for file_path in files_to_compress:
    if os.path.exists(file_path):
        dir_name = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        
        original_dir = os.getcwd()
        os.chdir(dir_name)
        
        subprocess.run(["zip", f"{file_name}.zip", file_name], check=True)
        print(f"Compressed {file_path}")
        
        os.remove(file_name)
        print(f"Removed {file_path}")
        
        os.chdir(original_dir)
