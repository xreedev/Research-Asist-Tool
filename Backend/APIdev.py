from flask import Flask, request, jsonify
import BART
import webcrawler as wc
app = Flask(__name__)


@app.route('/process_string', methods=['POST'])
def process_string():
    data = request.get_json()
    if 'input_string' not in data:
        return jsonify({'error': 'No input string provided'}), 400

    input_string = data['input_string']
    data=wc.extract_article_sections(input_string)
    data=BART.bartSummarize_dict(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
