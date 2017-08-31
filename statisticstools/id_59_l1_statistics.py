
l1_file = "/Users/liupeng/Documents/UM/dl2tcc/experiment/experiment results/id_61_train_1000_epoch_300_l1_loss.txt"

l1_mean_file = "/Users/liupeng/Documents/UM/dl2tcc/experiment/experiment results/id_59_train_500_epoch_300_l1_loss_mean.txt"

with open(l1_mean_file, "w") as ouput:
    with open(l1_file, "r") as infile:
        count = 0
        sum_l1 = 0.0
        for line in infile.readlines():
            if (count + 1) % 25 == 0:
                print((sum_l1 / 25))
                sum_l1 = float(line)
            else:
                sum_l1 += float(line)
            count += 1