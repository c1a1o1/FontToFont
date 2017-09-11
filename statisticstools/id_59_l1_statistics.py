
l1_file = "/Users/liupeng/Documents/UM/dl2tcc/experiment/experiment results/18_cgan_SOUR_train_loss.txt"

l1_mean_file = "/Users/liupeng/Documents/UM/dl2tcc/experiment/experiment results/18_cgan_SOUR_train_loss_mean.txt"

with open(l1_mean_file, "w") as ouput:
    with open(l1_file, "r") as infile:
        count = 0

        epoch_iter = 0

        epoch_10_ave = 0.0

        sum_l1 = 0.0
        for line in infile.readlines():
            if (count + 1) % 152 == 0:
                epoch_ave = sum_l1 / 152
                # print((sum_l1 / 152))
                sum_l1 = float(line)
                epoch_iter += 1

                if epoch_iter % 10 == 0:
                    print(epoch_10_ave / 10)
                    epoch_10_ave = 0.0
                else:
                    epoch_10_ave += epoch_ave

            else:
                sum_l1 += float(line)
            count += 1