from flask import Flask, request, jsonify
from transformers import T5Tokenizer, AutoModelForCausalLM
import time
import re

app = Flask(__name__)


@app.route("/", methods=["GET"])
def AIReplyAPI():
    message = request.args.get("message").rstrip().replace("？", "?")
    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
    model = AutoModelForCausalLM.from_pretrained("../output/yahooComment/")
    if "naroNovel_" in message:
        model = AutoModelForCausalLM.from_pretrained("../output/naroNovel/")
        message = message.replace("naroNovel_", "")
    input_token = tokenizer.encode(message, return_tensors="pt")
    result = model.generate(input_token, do_sample=True, max_length=50,
                            num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    output = tokenizer.batch_decode(result)[0]
    pattern = re.compile(message.replace("?", "\?"))
    output = pattern.sub("", output)
    output = re.sub(r"^</s> ", "", output)
    output = output.replace("</s>", "").replace("<unk> ",
                                                "").replace("<|endoftext|>", "")
    if output == "":
        output = "結果を出力できませんでした。AIの学習が不足しています。"
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=51400, debug=True)
