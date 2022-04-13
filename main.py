from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, UploadSet, IMAGES
from color_pallete import pallete_finder
from copy_image import copy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'randomstring'
app.config["UPLOADED_IMAGES_DEST"] = 'uploads'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class PhotoForm(FlaskForm):
    image = FileField('image')


@app.route('/', methods=["GET", "POST"])
def index():
    form = PhotoForm()

    if form.validate_on_submit():
        f = form.image.data
        filename = images.save(form.image.data)

        pallete = pallete_finder(f'uploads/{filename}')
        copy(filename)

        return render_template('color_pallete.html', pallete=pallete, filename=filename)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
