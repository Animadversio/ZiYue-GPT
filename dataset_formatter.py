import torch
import re
import os
import pickle as pkl
from glob import glob
from pathlib import Path

def sentence_spliter(full_text):
  book_sent = re.sub(r"。([^”’\n])", r"。\n\1", full_text)
  book_sent = re.sub(r"！([^”’\n])", r"！\n\1", book_sent)
  book_sent = re.sub(r"。”([^\n])", r"。”\n\1", book_sent)
  book_sent = re.sub(r"！”([^\n])", r"！”\n\1", book_sent)
  return book_sent


def test_sentence_spliter():
  sent = """臣闻不知而言不智，知而不言不忠，为人臣不忠当死，言而不当亦当死。虽然，臣愿悉言所闻，唯大王裁其罪。
  臣闻天下阴燕阳魏，连荆固齐，收韩而成从，将西面以与秦强为难，臣窃笑之。世有三亡，而天下得之，其此之谓乎！臣闻之曰：“以乱攻治者亡，以邪攻正者亡，以逆攻顺者亡。”今天下之府库不盈，囷仓空虚，悉其士民，张军数十百万。其顿首戴羽为将军，断死于前，不至千人，皆以言死。白刃在前，斧鑕在后，而却走不能死也。非其士民不能死也，上不能故也。言赏则不与，言罚则不行，赏罚不信，故士民不死也。
  今秦出号令而行赏罚，有功无功相事也。出其父母怀衽之中，生未尝见寇耳。闻战，顿足徒裼，犯白刃，蹈炉炭，断死于前者皆是也。夫断死与断生者不同，而民为之者，是贵奋死也。夫一人奋死可以对十，十可以对百，百可以对千，千可以对万，万可以克天下矣。今秦地折长补短，方数千里，名师数十百万。秦之号令赏罚、地形利害，天下莫若也。以此与天下，天下不足兼而有也。是故秦战未尝不克，攻未尝不取，所当未尝不破，开地数千里，此其大功也。然而兵甲顿，士民病，蓄积索，田畴荒，囷仓虚，四邻诸侯不服，霸王之名不成，此无异故，其谋臣皆不尽其忠也。
  臣敢言之，往者齐南破荆，东破宋，西服秦，北破燕，中使韩、魏，土地广而兵强，战克攻取，诏令天下。齐之清济浊河，足以为限；长城巨防，足以为塞。齐五战之国也，一战不克而无齐。由此观之，夫战者，万乘之存亡也。且闻之曰：“削迹无遗根，无与祸邻，祸乃不存。”秦与荆人战，大破荆，袭郢，取洞庭、五湖、江南，荆王君臣亡走，东服于陈。当此时也，随荆以兵则荆可举，荆可举，则民足贪也，地足利也。东以弱齐、燕，中以凌三晋。然则是一举而霸王之名可成也，四邻诸侯可朝也。而谋臣不为，引军而退，复与荆人为和，令荆人得收亡国，聚散民，立社稷，主置宗庙，令率天下西面以与秦为难，此固以失霸王之道一矣。天下又比周而军华下，大王以诏破之，兵至梁郭下，围梁数旬则梁可拔，拔梁则魏可举，举魏则荆、赵之意绝，荆、赵之意绝则赵危，赵危而荆狐疑，东以弱齐、燕，中以凌三晋。然则是一举而霸王之名可成也，四邻诸侯可朝也。而谋臣不为，引军而退，复与魏氏为和，令魏氏反收亡国，聚散民，立社稷，主置宗庙，令，此固以失霸王之道二矣。前者穰侯之治秦也，用一国之兵而欲以成两国之功。是故兵终身暴露于外，士民疲病于内，霸王之名不成，此固以失霸王之道三矣。
  赵氏，中央之国也，杂民所居也。其民轻而难用也。号令不治，赏罚不信，地形不便，下不能尽其民力。彼固亡国之形也，而不忧民萌。悉其士民，军于长平之下，以争韩上党。大王以诏破之，拔武安。当是时也，赵氏上下不相亲也，贵贱不相信也。然则邯郸不守。拔邯郸，管山东河间，引军而去，西攻修武，逾华，绛上党。代四十六县，上党七十县，不用一领甲，不苦一士民，此皆秦有也。以代、上党不战而毕为秦矣，东阳、河外不战而毕反为齐矣，中山、呼沱以北不战而毕为燕矣。然则是赵举，赵举则韩亡，韩亡则荆、魏不能独立，荆、魏不能独立则是一举而坏韩、蠹魏、拔荆，东以弱齐、燕，决白马之口以沃魏氏，是一举而三晋亡，从者败也。大王垂拱以须之，天下编随而服矣，霸王之名可成。而谋臣不为，引军而退，复与赵氏为和。夫以大王之明，秦兵之强，弃霸王之业，地曾不可得，乃取欺于亡国，是谋臣之拙也。且夫赵当亡而不亡，秦当霸而不霸，天下固以量秦之谋臣一矣。乃复悉士卒以攻邯郸，不能拔也，弃甲负弩，战竦而却，天下固已量秦力二矣。军乃引而复，并于孚下，大王又并军而至，与战不能克之也，又不能反运，罢而去，天下固量秦力三矣。内者量吾谋臣，外者极吾兵力。由是观之，臣以为天下之从，几不难矣。内者，吾甲兵顿，士民病，蓄积索，田畴荒，囷仓虚；外者、天下皆比意甚固。愿大王有以虑之也。"""

  print(sentence_spliter(sent))


def format_ctext_dataset():
  pkl_list = glob("ctext/*.pkl")
  chn_text_all = []
  for pkl_fn in pkl_list:
    data = pkl.load(open(pkl_fn, "rb"))
    chn_text_all.extend(data.chn_text_pool)
    # full text path
    txt_path = pkl_fn.replace(".pkl", ".txt")
    # full text split into sentences per line
    sent_path = pkl_fn.replace(".pkl", ".txt").replace("ctext", "ctext_sentence")
    book_fulltext = "".join(data.chn_text_pool)
    with open(txt_path, 'w') as f:
      f.write(book_fulltext)
    book_sent = sentence_spliter(book_fulltext)
    with open(sent_path, 'w') as f:
      f.write(book_sent)


if __name__ == '__main__':
  test_sentence_spliter()