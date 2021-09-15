# MountGodマニュアル

## MessageReaction.json
- keyWord(Array)：反応したい単語(String)
- reaction(Array)：付けたいリアクション(String)
    - デフォルト絵文字
        - [Emojipedia](https://emojipedia.org/) の **Codepoints**
        - 例. `U+12345`
    - カスタム絵文字
        - Discord内入力 `\:EmojiAlias:`
        - 例. `<:example:123456789012345678>`
- message(String)：言わせたい文章