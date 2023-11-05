from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def remove_silence(wav_path, output_path, silence_thresh=-40, min_silence_len=300):
    # 载入音频文件
    sound = AudioSegment.from_wav(wav_path)
    
    # 寻找非静音的块
    nonsilent_chunks = detect_nonsilent(
        sound,
        min_silence_len=min_silence_len,  # 最小的静音长度，单位为毫秒
        silence_thresh=silence_thresh     # 小于该值的为静音，默认为-16dBFS
    )
    
    # 合并非静音块
    non_silent_audio = sum([sound[start:end] for start, end in nonsilent_chunks])
    
    # 导出结果
    non_silent_audio.export(output_path, format="wav")

# 使用函数去除空白部分
remove_silence("prompts/dr-cut.wav", "prompts/dr-short.wav")
