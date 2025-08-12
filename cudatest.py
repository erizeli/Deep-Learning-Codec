import torch

print(torch.cuda.is_available())  # Should be True if GPU + CUDA are ready
print(torch.cuda.get_device_name(0))  # If True, prints GPU name