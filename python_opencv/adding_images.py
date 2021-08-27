# def im_sum(im_1, im_2):
#     r1, g1, b1 = cv.split(im_1)
#     r2, g2, b2 = cv.split(im_2)
#
#     r_out = channel_sum(r1, r2)
#     g_out = channel_sum(g1, g2)
#     b_out = channel_sum(b1, b2)
#
#     # print(r1[474][200])
#     # print(r2[474][200])
#     # print(r_check[474][200])
#
#     # for f in range(len(r1)):
#     #     for v in range(len(r1[0])):
#     #         if r1[f][v] > 150 and r2[f][v] > 50:
#     #             print(r1[f][v])
#     #             print(r2[f][v])
#     #             print('values', f, v)
#
#     out = np.dstack((r_out, g_out, b_out))
#
#     return out


# def channel_sum(channel_1, channel_2):
#     ch_aux = []
#     if not same_channel_size(channel_1, channel_2):
#         return -1
#     else:
#         for i in range(len(channel_1)):
#             for j in range(len(channel_1[0])):
#                 a = channel_1[i][j]
#                 b = channel_2[i][j]
#                 ch_sum_aux = a + b
#                 if a != 0 and b != 0 and a + b > 250:
#                     print(a, b)
#                 if ch_sum_aux > 255:
#                     ch_aux.append(np.int8(ch_sum_aux - (channel_1[i][j] if channel_1[i][j] < channel_2[i][j]
#                                                         else channel_2[i][j])))
#                 else:
#                     ch_aux.append(channel_1[i][j] + channel_2[i][j])
#         channel_out = np.array(ch_aux)
#         channel_out = np.reshape(channel_out, (len(channel_1), len(channel_1[0])))
#         return channel_out


# def same_channel_size(channel_1, channel_2):
#     if len(channel_1) == len(channel_2) and len(channel_1[0]) == len(channel_2[0]):
#         return True
#     else:
#         return False


# def pixel_over_value(input_channel):
#     i_vec_aux = []
#     for i in range(len(input_channel)):
#         for j in range(len(input_channel[0])):
#             if input_channel[i][j] > 255:
#                 print(input_channel[i][j])
#                 i_vec_aux.append(255 - input_channel[i][j])
#             else:
#                 i_vec_aux.append(input_channel[i][j])
#     out_channel = np.array(i_vec_aux)
#     out_channel = np.reshape(out_channel, (int(len(input_channel)), int(len(input_channel[0]))))
#     return out_channel
