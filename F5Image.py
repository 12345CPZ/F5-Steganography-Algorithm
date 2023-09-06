#coding: utf-8
from io import BytesIO
from PIL import Image
from jpeg_encoder import JpegEncoder as F5JpegEncoder
import jpeg_extract
import StringIO

# 执行 F5 编码过程。
#
# 执行后将在指定的文件路径处生成一个 jpg 文件。 
#
# - Parameter image_file_name: 想要执行 F5 编码的图片文件的路径。
# - Parameter image_output_path: 执行完成后输出的 jpg 文件路径。扩展名必须是 `jpg`。
# - Parameter password: 用于初始化随机数发生器的密码。
# - Parameter embbed_data: 想要嵌入的数据。可以是任何形式的文件数据。例如，可以传入字符串 "nini"。
def F5Eecoder(image_file_path, image_output_path, password, embbed_data):
    print('--- Processing F5 Encoder......')
    print('--- password = ' + password)
    print('--- embbed_data = ' + embbed_data)
    print('--- [耗时较长, 请等待] ---')
    print('---------------------------')
    pyoutput = StringIO.StringIO()
    pyimage = Image.open(image_file_path)
    image_encoder = F5JpegEncoder(pyimage, 80, pyoutput, '')
    image_encoder.compress(embbed_data, password)
    pyarray = pyoutput.getvalue()
    pyoutput.close()
    with open(image_output_path, 'wb') as file:
        file.write(pyarray)
    print('--- Finished.')
    print('---------------------------')


# 执行 F5 解码过程。
#
# 执行后将在指定的文件路径处生成解密文件。
#
# - Parameter image_file_path: 想要执行 F5 解码的图片文件的路径。
# - Parameter output_file_path: 本函数执行完成后将把 隐秘信息 存储到该路径对应的文件。
# - Parameter password: 用于初始化随机数发生器的密码。
def F5Decoder(image_file_path, output_file_path, password):
    print('--- 执行 F5 解码....')

    print('--- 密码: ' + password)
    print('--- [耗时较长, 请等待] ---')
    output_string_io = StringIO.StringIO()
    input_stream = open(image_file_path, 'rb')
    jpeg_extract.JpegExtract(output_string_io, password).extract(input_stream.read())
    output_stream_array = output_string_io.getvalue()
    input_stream.close()
    output_string_io.close()
    print('--- 解码成功')
    # 写入文件
    with open(output_file_path, 'wb') as file:
            file.write(output_stream_array)

# 执行测试
#
# 这将以 `图片P.jpg`` 为原图，`PASSWORD` 为密码，生成嵌入了隐秘信息 `深圳杯数学建模挑战赛`的文件。输出文件名为 `图片SP.jpg`。
# 然后对 `图片SP.jpg` 执行 F5 解码，解码后得到的隐秘信息存储在 `output_data.txt` 中。
def test_F5():
    F5Eecoder(r"图片P.jpg", "图片SP.jpg", 'PASSWORD', "深圳杯数学建模挑战赛")

    F5Decoder(r"图片SP.jpg", '图片output_data.txt', 'PASSWORD')

test_F5()