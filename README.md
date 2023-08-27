```
   Turkish
```
# Discord Keylogger Bot

Bu proje, bir Discord botu aracılığıyla klavye girdilerini toplamak ve belirtilen bir kanala iletmek için oluşturulmuştur. Proje sahibi olarak, bu projenin kullanımından kaynaklanan sorumlulukların size ait olduğunu unutmayın. 

## Nasıl Kullanılır

1. Öncelikle projeyi başlatmak için aşağıdaki adımları izleyin:

   - Gerekli Python modüllerini yüklemek için aşağıdaki komutları kullanın:
     ```
     pip install pynput discord.py
     ```
   - `main.py` dosyasındaki `token` ve `channelID` değerlerini Discord botunuzun token'ı ve istediğiniz kanalın ID'si ile değiştirin.
   - Projeyi başlatmak için terminalde aşağıdaki komutu kullanın:
     ```
     python main.py
     ```

2. Bot başlatıldığında, klavye girdileri kaydedilmeye başlar ve bu girdiler botun bulunduğu Discord sunucusundaki belirli bir kanala iletilir.

3. İstediğiniz zaman, botun bulunduğu kanalda `!` komutunu kullanarak kaydedilen girdileri alabilirsiniz.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.

---

*Not: Bu proje sadece eğitim amaçlı oluşturulmuş bir örnektir. Başkalarının gizlilik haklarını ihlal etmek veya kötüye kullanmak, yasalar ve etik kurallar tarafından yasaklanmıştır. Lütfen etik ve yasal kurallara uygun şekilde hareket edin.*

```
   English
```

# Discord Keylogger Bot

This project is created to capture keyboard inputs through a Discord bot and send them to a specified channel. As the project owner, please note that you are responsible for the usage of this project.

## How to Use

1. To start the project, follow the steps below:

   - Use the following commands to install the required Python modules:
     ```
     pip install pynput discord.py
     ```
   - Replace the `token` and `channelID` values in the `main.py` file with your Discord bot's token and the ID of the desired channel.
   - Start the project by using the following command in the terminal:
     ```
     python main.py
     ```

2. When the bot is started, it will begin recording keyboard inputs, and these inputs will be sent to a specific channel on the Discord server where the bot is present.

3. At any time, you can retrieve the recorded inputs in the channel where the bot resides by using the `!` command.

## License

This project is licensed under the MIT License. You can review the details in the [LICENSE](LICENSE) file.

---

*Note: This project is intended for educational purposes only. Violating others' privacy or misuse is prohibited by laws and ethical standards. Please act in accordance with ethical and legal rules.*
