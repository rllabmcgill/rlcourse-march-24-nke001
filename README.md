I am presenting the paper "Model Free Episodic Control" https://arxiv.org/abs/1606.04460. 

The slides are in Model Free Episodic Control.pdf, and the code and experimental results are in the code/* directory.

To run the code, run `python run_episodic_control --roms/space_invader.bin`

To run analysis, run `python analysis.py log_space_k11.txt`

To compare results from different models, run `python analysis_compare.py log_space_k11.txt log_space_k5.txt`
