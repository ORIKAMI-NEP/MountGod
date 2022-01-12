from flask import Flask, jsonify, request
from transformers import T5Tokenizer, AutoModelForCausalLM
import time
import re

app = Flask(__name__)


@app.route("/", methods=["GET"])
def AIReplyAPI():
    message = request.args.get("message").rstrip().replace("？", "?")
    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
    model = AutoModelForCausalLM.from_pretrained("../output/yahooComment/")
    if "\\naroNovel" in message:
        model = AutoModelForCausalLM.from_pretrained("../output/naroNovel/")
        message = message.replace("\\naroNovel", "")
    startTime = time.time()
    input_token = tokenizer.encode(message, return_tensors="pt")
    result = model.generate(input_token, do_sample=True, max_length=20,
                            num_return_sequences=1, pad_token_id=tokenizer.eos_token_id, max_time=60.0)
    output = tokenizer.batch_decode(result)[0]
    pattern = re.compile(message.replace("?", "\?"))
    output = pattern.sub("", output)
    output = re.sub(r"^</s> ", "", output)
    output = output.replace("</s>", "").replace("<unk> ",
                                                "").replace("<|endoftext|>", "")
    if output is None:
        # return jsonify({"結果を出力できませんでした。AIの学習が不足しています。"})
        return "結果を出力できませんでした。AIの学習が不足しています。"
    else:
        # return jsonify({output+" ( %.5f [sec] )" % (time.time() - startTime)})
        return output+" ( %.5f [sec] )" % (time.time() - startTime)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=51400, debug=True)
