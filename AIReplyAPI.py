from flask import Flask, jsonify, request
from transformers import T5Tokenizer, AutoModelForCausalLM
import time
import re

app = Flask(__name__)

tokenizer = T5Tokenizer.from_pretrained("../rinna/japanese-gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("../output/novel/")


@app.route("/", methods=["GET"])
def AIReplyAPI():
    message = request.args.get("message").rstrip().replace("？", "?")
    if "novel" in message:
        model = AutoModelForCausalLM.from_pretrained("../output/novel/")
    startTime = time.time()
    input_token = tokenizer.encode(message, return_tensors="pt")
    result = model.generate(input_token, do_sample=True, max_length=20,
                            num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    output = tokenizer.batch_decode(result)[0]
    pattern = re.compile(message.replace("?", "\?"))
    output = pattern.sub("", output)
    output = re.sub(r"^</s> ", "", output)
    output = output.replace("</s>", "").replace("<unk> ",
                                                "").replace("<|endoftext|>", "")
    return jsonify({output+" ( %.5f [sec] )" % (time.time() - startTime)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=51401, debug=True)
