import pickle
import numpy as np

src = "../../experiment/data6772/train.obj"

with open(src, "rb") as of:
    examples = list()
    while True:
        try:
            e = pickle.load(of)
            examples.append(e)
            if len(examples) % 1000 == 0:
                print("processed %d examples" % len(examples))
        except EOFError:
            break
        except Exception:
            pass


    print(examples[0])

    first = np.array(examples[0])
    f_max = np.amax(first)
    f_min = np.amin(first)

    print("max :{} - min: {}".format(f_max, f_min))