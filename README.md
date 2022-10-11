# ZiYue-GPT (子曰 生成器)
This is a hobbyist project to train a generative Language model (GPT2) to output ancient chinese text, simulating the style of talkings and writing for ancient Chinese philosophers. 

It's divided into these procedures
* Collecting Chinese classics from online sources. 
  * and perhaps ther English and modern Chinese translation
* Clean up text to make a dataset 
* Train GPT2 based on these text dataset. 
* Enjoy the generated text! 

## Notebooks
* [Data Collection](https://colab.research.google.com/drive/1Wehm6Fd812-LWMNKrIJCMCeQjcyu7__Y?usp=sharing)
* [Formatting and GPT training](https://colab.research.google.com/drive/1vIgEBvXFMqehq4yHl1tEYksVBjsU9V2K?usp=sharing)

## Sample Text

### 8 Layer GPT after 120 epochs

```python
In [140]: generator("子曰", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[140]:
[{'generated_text': '子曰 ： 君 子 不 终 穷 贱 ， 学 之 道 也 。 怀 之 言 曰 ： 古 之 学 ， 无 欲 而 学 ， 是 其 德 不  学 也 。 子 ， 今 死 而 后 无 闻 。 进 。 文 也 。 也'},
```

```python
In [160]: generator("子曰", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[160]:
[{'generated_text': '子曰 ： 先 志 之 以 仁 ， 民 之 以 礼 。 ， 命 之 以 德 ， 齐 之 以 礼 ， 则 民 有 耻 且 格 。 子  ， 何 其 齐 ！ 子 焉 。 文 王 之 深 矣 哉 ！'},
```

```python
In [145]: generator("秦王", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[145]:
[{'generated_text': '秦王 曰 ： 寡 人 固 未 有 分 地 ， 易 服 寡 人 者 ， 非 寡 人 之 愿 也 。 若 是 ， 则 非 欺 寡 人  也 。 敝 矣 。 。 无 术 也 。'},
```


```python
In [153]: generator("子路对曰", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[153]:
[{'generated_text': '子路对曰 ： 君 病 ， 病 而 后 言 。 子 病 ， 子 病 而 死 。 死 。 病 ， 病 薨 。 。 。 崩 ， 子 反 乡 。 病 ， 代 代 。 。'},
```

```python
In [156]: generator("庄子曰", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[156]:
[{'generated_text': '庄子曰 ： 吾 自 卫 反 也 。 里 子 曰 ： 父 老 矣 ， 不 足 以 为 齿 。 子 也 。 子 ， 盖 子 产 。 子 。 也 。 子 曰 ：'},
```

```python
In [152]: generator("鲲鹏", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[152]:
{'generated_text': '鲲鹏 之 背 ， 不 知 其 几 千 里 也 。 视 而 不 得 一 鼓 耳 。 以 其 无 知 也 。 然 则 行 矣 。 然  而 不 待 乎 ？ 文 王 曰 ：'},
```

```python
In [157]: generator("鲲鹏", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[157]:
[{'generated_text': '鲲鹏 为 两 翼 ， 天 下 乃 通 。 氏 文 姬 ， 生 周 公 ， 辅 晋 作 纪 ， 盖 太 公 立 。 之 所 谓 尊  上 帝 命 也 。 若 曰 ： 伯 禽 曰 ： 书 正'},
```

```python
In [158]: generator("鲲鹏", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[158]:
[{'generated_text': '鲲鹏 能 能 言 之 ， 不 能 自 悔 ； 尧 舜 之 义 ， 不 能 法 之 。 虽 桀 之 贤 ， 亦 不 能 得 也 。  愿 绝 矣 。 无 以 为 胡 。 闻 。 。'},
```

```python
In [139]: generator("鲲鹏", max_length=60, num_return_sequences=5, num_beams=10,  repetition_penalty=1.5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[139]:
[{'generated_text': '鲲鹏 之 来 兮 ， 吾 知 之 矣 ！ 其 无 知 ！ 也 而 不 知 ！ 其 犹 戒 矣 。 之 学 者 ， 吾 未 知 也  。 此 言 之 谓 也 。 也 。 离 已 。'},
```
