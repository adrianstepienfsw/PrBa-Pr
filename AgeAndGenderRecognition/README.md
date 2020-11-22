## Gdzie muszą znajdować się dane?

w folderze:
data/images/aligned/
mają znajdować się foldery ze zdjęciami, które ściągamy z https://talhassner.github.io/home/projects/Adience/Adience-data.html#agegender (wersja aligned).

## Utworzenie zbiorów danych z etykietami Age

```
$ python src/preproc.py --fold_dir data/folds/train_val_txt_files_per_fold/test_fold_is_0 --train_list age_train.txt --valid_list age_val.txt --data_dir data/images/aligned --output_dir data/folds/tf/age_test_fold_is_0
```

## Utworzenie zbiorów danych z etykietami Gender

```
$ python src/preproc.py --fold_dir data/folds/train_val_txt_files_per_fold/test_fold_is_0 --train_list gender_train.txt --valid_list gender_val.txt --data_dir data/images/aligned --output_dir data/folds/tf/gen_test_fold_is_0
```

## Uruchomienie uczenia Age

```
$ python src/train.py --train_dir data/folds/tf/age_test_fold_is_0
```

## Uruchomienie uczenia Gender

```
$ python src/train.py --train_dir data/folds/tf/gen_test_fold_is_0 --batch_size 64 --max_steps 30000 --eta 0.001
```
