"""Process client requests"""

import os
import datetime

from flask import Flask, request, json
from flask_cors import CORS

from src.slide import Slide
from src.lang import LangChecker

# create app instance with CORS
app = Flask(__name__)
cors = CORS(app)

tool = LangChecker()


@app.post('/slide_analyze/')
def analyze_slide():
    """Extract slide and analyze for improvements

    Returns:
        dict[str,str]: response
    """
    slide = Slide(request.json['url'], datetime.datetime.now().strftime(
        '%m_%d_%Y_%H_%M_%S') + '.pptx')
    slide.extract_pptx()

    info = slide.get_data()

    # check for spelling and grammatical errors
    tool.analyze_txt(slide.get_txt())
    suggestions = tool.get_results()

    # delete slide after processing
    if os.path.exists(slide.filename):
        os.remove(slide.filename)

    return {
        'slide_count': info[0],
        'word_count': json.dumps(info[1]),
        'shape_count': info[2],
        'font_count': json.dumps(info[3]),
        'mistake': json.dumps(suggestions)
    }


# main thread
if __name__ == '__main__':
    app.run(port=5000)
