userReply = input("Apakah Anda ingin mengirim paket? (Ketik ya atau tidak) ")
if userReply == "ya":
    print("Kami dapat membantu Anda untuk mengirimkan paket!")
else:
    print("Silakan datang kembali bila Anda ingin mengirimkan paket. Terima kasih.")
#Working with Statement
userReply = input("Apakah Anda mau membeli materai, amplop atau mau foto copy? (Ketik materai, amplop atau foto copy) ")
if userReply == "materai":
    print("Kami menyediakan beberapa design yang bisa Anda pilih.")
elif userReply == "amplop":
    print("Ada tersedia beberapa ukuran amplop.")
elif userReply == "foto copy":
    copies = input("Mau foto copy berapa kali? (Ketik angkanya) ")
    print("Ini foto copynya rangkap {}.".format(copies))
else:
    print("Terima kasih, silakan datang kembali.")
