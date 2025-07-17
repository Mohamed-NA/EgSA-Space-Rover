Null = 0
Valid = 1
Invalid = 0
Dest_Index = 1
Source_Index = 0
Data_Length_Index = 4
Packet_Type_Index = 2
Brain_Address = 11
Ping = 4
GetCam = 5
MAP = 6
ACK = 1


def crc_calc(data: bytearray):
    poly = 0x8408
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)

    crc = (crc & 0xFFFF)
    return crc


def ssp_construction(header: bytearray, data: bytearray, data_length):
    x = []
    x[0:3] = header
    x[4: 4 + data_length] = data
    crc = crc_calc(bytearray(x))
    x.append(crc >> 8)
    x.append(crc & 0xFF)
    z = [0xc0]
    z.extend(x)
    z.append(0xc0)
    return z


def frame_validation(ssp_frame: bytearray, length):
    var_x = ssp_frame.copy()
    del var_x[-2:]
    crc = crc_calc(var_x)

    if (crc >> 8) == ssp_frame[length - 2]:
        if (crc & 0xFF) == ssp_frame[length - 1]:
            return Valid
        else:
            return Invalid
    else:
        return Invalid


def data_extraction(ssp_frame: bytearray, length):
    i = 0
    Data_Output: bytearray

    while i < length:
        if ssp_frame[i] == 0xc0:

            l = int(ssp_frame[i + Data_Length_Index])
            if ssp_frame[l + 7 + i] == 0xc0:

                ssp_without_flag = []
                ssp_without_flag.extend(ssp_frame[i + 1: l + 7 + i])
                print(f"\nssp_without_flag: {ssp_without_flag}")

                if frame_validation(ssp_without_flag, l + 6) == Valid:
                    data_output = ssp_without_flag[4:-2]
                    return data_output

                else:
                    i = i + 1

                    if i < length - 7:
                        continue
                    else:
                        return 500

            else:
                i = i + 1
                if i < length - 7:
                    continue
                else:
                    return 500

        else:
            i = i + 1
            if i < length - 7:
                continue
            else:
                return 500


def response(header: bytearray, data: bytearray, response_out: bytearray):
    temp = header[Source_Index]
    header[Source_Index] = header[Dest_Index]
    header[Dest_Index] = temp
    command = int(header[Packet_Type_Index])

    if command == Ping:
        type_num = ACK
        print("\nPing")
        ssp_construction(header, [0], 0)

    elif command == GetCam:
        type_num = ACK
        print("\nGetCam")
        ssp_construction(header, [0], 0)

    elif command == MAP:
        type_num = ACK
        print("\nMAP")
        ssp_construction(header, [0], 0)

    else:
        return 500

    return type_num
