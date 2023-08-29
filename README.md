```
   Turkish
```
# Discord Keylogger Bot

Bu proje, bir Discord botu aracılığıyla klavye girdilerini toplamak ve belirtilen bir kanala iletmek için oluşturulmuştur. Proje sahibi olarak, bu projenin kullanımından kaynaklanan sorumlulukların size ait olduğunu unutmayın. 

Sorumluluk Projeyi Yapan Kişiye Yani Serhan Bakır'a Ait Değildir Sadece Eğitim Amaçlı Yazılmıştır

## Nasıl Kullanılır

1. Öncelikle projeyi başlatmak için aşağıdaki adımları izleyin:

   - Gerekli Python modüllerini yüklemek için aşağıdaki komutları kullanın:
     ```
     pip install pynput discord.py threading subprocess os shutil sys pyinstaller
     ```
   - `main.py` dosyasındaki `token` ve `channelID` değerlerini Discord botunuzun token'ı ve istediğiniz kanalın ID'si ile değiştirin.
   - Projeyi Exe dosyası halina getirmek için aşağıdaki komutu terimale yazınız bu exe dosyası ana dizinde dis klasörü altında oluşacaktır
     ```
     pyinstaller --onefile main.py
     ```
   - Projeyi başlatmak için terminalde aşağıdaki komutu kullanın:
     ```
     python main.py
     ```
2. Proje başlatıldığında, kendini AppData'nın içindeki Roaming klasörünün içine kopyalar ve bilgisayarı her yeniden başlattığında bu exe dosyası çalışmaya başlar

3. Bot başlatıldığında, klavye girdileri kaydedilmeye başlar ve bu girdiler botun bulunduğu Discord sunucusundaki belirli bir kanala iletilir.

4. İstediğiniz zaman, botun bulunduğu kanalda `!` komutunu kullanarak kaydedilen girdileri alabilirsiniz.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.

---

*Not: Bu proje sadece eğitim amaçlı oluşturulmuş bir örnektir. Başkalarının gizlilik haklarını ihlal etmek veya kötüye kullanmak, yasalar ve etik kurallar tarafından yasaklanmıştır. Lütfen etik ve yasal kurallara uygun şekilde hareket edin.*

```
   English
```

# Discord Keylogger Bot

This project is created to capture keyboard inputs through a Discord bot and send them to a specified channel. As the project owner, please note that you are responsible for the usage of this project.

Responsibility does not belong to the person who made the project, namely Serhan Bakır. It was written for educational purposes only.

## How to Use

1. To start the project, follow the steps below:

   - Use the following commands to install the required Python modules:
     ```
     pip install pynput discord.py threading subprocess os shutil sys pyinstaller
     ```
   - Replace the `token` and `channelID` values in the `main.py` file with your Discord bot's token and the ID of the desired channel.
   - To make the project Exe file, type the following command. This exe file will be created in dis parts in the main directory.
     ```
     pyinstaller --onefile main.py
     ```
   - Start the project by using the following command in the terminal:
     ```
     python main.py
     ```
2. When the project is started, it copies itself into the Roaming folder in AppData and this exe file starts running every time you restart the computer.

3. When the bot is started, it will begin recording keyboard inputs, and these inputs will be sent to a specific channel on the Discord server where the bot is present.

4. At any time, you can retrieve the recorded inputs in the channel where the bot resides by using the `!` command.

## License

This project is licensed under the MIT License. You can review the details in the [LICENSE](LICENSE) file.

---

*Note: This project is intended for educational purposes only. Violating others' privacy or misuse is prohibited by laws and ethical standards. Please act in accordance with ethical and legal rules.*
