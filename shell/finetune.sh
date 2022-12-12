# sh finetune.sh naroNovel
python3 transformers/examples/language-modeling/run_clm.py --model_name_or_path=rinna/japanese-gpt2-small --train_file=data/data.train.txt --validation_file=data/data.validation.txt --do_train --do_eval --num_train_epochs=3 --save_steps=5000 --save_total_limit=3 --per_device_train_batch_size=1 --per_device_eval_batch_size=1 --output_dir=output/$1/ --use_fast_tokenizer=False
