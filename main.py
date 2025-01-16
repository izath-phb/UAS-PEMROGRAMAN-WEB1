from flask import Flask, render_template, redirect, request, url_for
from DB_Operations import add_text, get_data, update_text, get_data_by_id, delete_text

app = Flask(__name__)

# Route untuk halaman utama
@app.route("/")
@app.route("/websitekesehatan")
def website_kesehatan():
    data = get_data()  # Ambil semua data dari database
    return render_template('kesehatan.html', data=data)

# Route untuk halaman edit data berdasarkan ID
@app.route('/kesehatan_edit/<int:id>', methods=["GET", "POST"])
def edit_kesehatan(id):
    if request.method == "POST":
        # Update data jika metode POST
        topik_value = request.form["topik"]
        deskripsi_value = request.form["deskripsi"]
        updated = update_text(id, topik_value, deskripsi_value)
        if updated:
            return redirect(url_for('website_kesehatan'))
        else:
            return "Failed to update data", 500
    else:
        # Ambil data untuk di-edit jika metode GET
        data = get_data_by_id(id)
        return render_template('kesehatan_edit.html', data=data)

# Route untuk menghapus data
@app.route('/kesehatan_delete/<int:id>')
def delete_kesehatan(id):
    deleted = delete_text(id)
    if deleted:
        return redirect(url_for('website_kesehatan'))  # Kembali ke halaman utama setelah delete
    else:
        return "Failed to delete data", 500

# Route untuk menambahkan data baru
@app.route('/add_text', methods=["POST", "GET"])
def add_kesehatan():
    if request.method == "POST":
        # Tambahkan data baru jika metode POST
        topik_value = request.form["topik"]
        deskripsi_value = request.form["deskripsi"]
        add_new = add_text(topik_value, deskripsi_value)
        if add_new:
            return redirect(url_for('website_kesehatan'))  # Kembali ke halaman utama
        else:
            return "Failed to add data", 500
    else:
        # Render halaman untuk menambahkan data
        return render_template('kesehatan.html')

if __name__ == "__main__":
    app.run(debug=True)
