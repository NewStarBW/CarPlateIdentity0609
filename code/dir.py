# 初夏 2024/6/9 20:33 dir
import os

# 获取当前工作目录
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '../carIdentityData/model/char_recongnize/model.ckpt-600.meta')
checkpoint_path = os.path.join(current_dir, '../carIdentityData/model/char_recongnize/model.ckpt-600')

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model meta file not found: {model_path}")
if not os.path.exists(checkpoint_path + '.index'):
    raise FileNotFoundError(f"Checkpoint file not found: {checkpoint_path}")

print("Both model and checkpoint files exist.")
