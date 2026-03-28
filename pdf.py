import pikepdf

old_pdf = pikepdf.Pdf.open("/home/samarth/folder/notes.pdf")

no_extract = pikepdf.Permissions(extract=False)

old_pdf.save(
    "/home/samarth/folder/pro_new.pdf",
    encryption=pikepdf.Encryption(
        user="123abc",
        owner="samarth",
        allow=no_extract
    )
)

print("Protected PDF created successfully!")