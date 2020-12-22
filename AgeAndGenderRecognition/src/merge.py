def main():
    f_age = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/age_train.txt", "r")
    f_merged = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/age_gender_train.txt", "w")

    for x1 in f_age:
        f_gender = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/gender_train.txt", "r")
        found = False
        for x2 in f_gender:
            if(x1.split(" ")[0] == x2.split(" ")[0]):
                f_merged.write(x1.split(" ")[0]+" "+x1.split(" ")[1][0]+" " + x2.split(" ")[1])
                found = True
                break;


    f_age = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/age_test.txt", "r")
    f_merged = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/age_gender_test.txt", "w")


    for x1 in f_age:
        f_gender = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/gender_test.txt", "r")
        found = False
        for x2 in f_gender:
            if(x1.split(" ")[0] == x2.split(" ")[0]):
                f_merged.write(x1.split(" ")[0]+" "+x1.split(" ")[1][0]+" " + x2.split(" ")[1])
                found = True
                break;

    f_age = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/age_val.txt", "r")
    f_merged = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/age_gender_val.txt", "w")


    for x1 in f_age:
        f_gender = open("data/folds/train_val_txt_files_per_fold/test_fold_is_0/gender_val.txt", "r")
        found = False
        for x2 in f_gender:
            if(x1.split(" ")[0] == x2.split(" ")[0]):
                f_merged.write(x1.split(" ")[0]+" "+x1.split(" ")[1][0]+" " + x2.split(" ")[1])
                found = True
                break;



if __name__ == '__main__':
    main()