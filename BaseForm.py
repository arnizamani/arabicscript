# Format:
# Dictionary where
# key: is an Arabic letter (only letters are included, no other characters such as
#   diacritic marks and punctuation marks)
# value: the base form of the key (dotless and without any marks), which is either
#       — a single character (string): number of dots is assumed to be zero
#       — a pair with:
#           0: a single character (string)
#           1: number of dots, which is either:
#               — a single number (number of dots)
#               — a pair where:
#                   0: number of dots in isolated and final forms
#                   1: number of dots in initial and medial forms

base_form = {
    # Hamza
    chr(0x0621): (chr(0x0621), 0),  # Hamza
    chr(0x06FD): (chr(0x0621), 0),  # Sindhi Aeen
    # Alef
    chr(0x0622): (chr(0x0627), 0),  # alef with maddah above
    chr(0x0623): (chr(0x0627), 0),  # alef with hamza above
    chr(0x0625): (chr(0x0627), 0),  # alef with hamza below
    chr(0x0627): (chr(0x0627), 0),  # alef
    chr(0x0671): (chr(0x0627), 0),  # hamzat al-wasl
    chr(0x0672): (chr(0x0627), 0),  # alef with wavy hamza above
    chr(0x0673): (chr(0x0627), 0),  # alef with wavy hamza below
    chr(0x0675): (chr(0x0627), 0),  # high hamza alef
    chr(0x0773): (chr(0x0627), 0),  # alef with two above
    chr(0x0774): (chr(0x0627), 0),  # alef with three above
    chr(0x08AD): (chr(0x08AD), 0),  # low alef
    # Beh
    chr(0x0628): (chr(0x066E), 1),  # Beh
    chr(0x062A): (chr(0x066E), 2),  # Teh
    chr(0x062B): (chr(0x066E), 3),  # Theh
    chr(0x066E): (chr(0x066E), 0),  # Dotless Beh
    chr(0x0679): (chr(0x066E), 0),  # Tteh (Teh with small V)
    chr(0x067A): (chr(0x066E), 2),  # Tteheh (Teh with two dots vertical above)
    chr(0x067B): (chr(0x066E), 2),  # Beeh (Beh with two dots vertical below)
    chr(0x067C): (chr(0x066E), 2),  # Teh with ring
    chr(0x067D): (chr(0x066E), 3),  # Teh with three dots above downwards
    chr(0x067E): (chr(0x066E), 3),  # Peh
    chr(0x067F): (chr(0x066E), 4),  # Teheh (Beh with four dots above)
    chr(0x0680): (chr(0x066E), 4),  # Beheh (Beh with four dots below)
    chr(0x0750): (chr(0x066E), 3),  # Beh with three dots horizontally below
    chr(0x0751): (chr(0x066E), 4),  # Seh with dot below
    chr(0x0752): (chr(0x066E), 3),  # Dotless Beh with three dots pointing upwards below
    chr(0x0753): (chr(0x066E), 5),  # Teh with three dots pointing upwards below
    chr(0x0754): (chr(0x066E), 3),  # Beh with two dots below and dot above
    chr(0x0755): (chr(0x066E), 0),  # Beh with inverted small V below
    chr(0x0756): (chr(0x066E), 0),  # Beh with small V (above)
    chr(0x08A0): (chr(0x066E), 0),  # Dotless Beh with V below
    chr(0x08A1): (chr(0x066E), 1),  # Beh with hamza above
    chr(0x08B6): (chr(0x066E), 1),  # Beh with small meem above
    chr(0x08B7): (chr(0x066E), 3),  # Peh with small meem above
    chr(0x08B8): (chr(0x066E), 2),  # Dotless Beh with small teh above
    # Teh Marbuta
    chr(0x0629): (chr(0x06D5), 2),  # Teh Marbuta
    chr(0x06D5): (chr(0x06D5), 0),  # Ae (Dotless Teh Marbuta)
    chr(0x06C0): (chr(0x06D5), 0),  # Dotless Teh Marbuta With Hamza Above
    chr(0x06C3): (chr(0x06C1), 2),  # Teh Marbuta Goal (Urdu Heh)
    # Hah
    chr(0x062C): (chr(0x062D), 1),  # Jeem
    chr(0x062D): (chr(0x062D), 0),  # Hah
    chr(0x062E): (chr(0x062D), 1),  # Khah
    chr(0x0681): (chr(0x062D), 0),  # Hah with hamza above
    chr(0x0682): (chr(0x062D), 2),  # Hah with two dots vertical above
    chr(0x0683): (chr(0x062D), 2),  # Nyeh (Hah with two dots horizontally below)
    chr(0x0684): (chr(0x062D), 2),  # Dyeh (Hah with two dots vertically below)
    chr(0x0685): (chr(0x062D), 3),  # Hah with three dots above
    chr(0x0686): (chr(0x062D), 3),  # Tcheh (Hah with three dots below)
    chr(0x0687): (chr(0x062D), 4),  # Tcheheh (Hah with four dots below)
    chr(0x06BF): (chr(0x062D), 4),  # Tcheh with dot above
    chr(0x0757): (chr(0x062D), 2),  # Hah with two dots above (horizontal)
    chr(0x0758): (chr(0x062D), 3),  # Hah with three dots pointing upwards below
    chr(0x076E): (chr(0x062D), 0),  # Hah with tah in the middle
    chr(0x076F): (chr(0x062D), 2),  # Hah with two dots vertical and tah in the middle
    chr(0x0772): (chr(0x062D), 0),  # Hah with small tah above
    chr(0x077C): (chr(0x062D), 0),  # Hah with four in the middle
    chr(0x08A2): (chr(0x062D), 3),  # Jeem with two dots above
    # Dal
    chr(0x062F): (chr(0x062F), 0),  # Dal
    chr(0x0630): (chr(0x062F), 1),  # Thal (Dal with dot above)
    chr(0x0688): (chr(0x062F), 0),  # Ddal (Dal with small tah)
    chr(0x0689): (chr(0x062F), 0),  # Dal with ring
    chr(0x068A): (chr(0x062F), 1),  # Dal with dot below
    chr(0x068B): (chr(0x062F), 1),  # Dal with dot below and small tah
    chr(0x068C): (chr(0x062F), 2),  # Dahal (Dal with two dots above)
    chr(0x068D): (chr(0x062F), 2),  # Ddahal (Dal with two dots below)
    chr(0x068E): (chr(0x062F), 3),  # Dul (Dal with three dots above)
    chr(0x068F): (chr(0x062F), 3),  # Dal with three dots above downwards
    chr(0x0690): (chr(0x062F), 4),  # Dal with four dots above
    chr(0x06EE): (chr(0x062F), 0),  # Dal with inverted V
    chr(0x0759): (chr(0x062F), 2),  # Dal with two dots vertically below and small tah
    chr(0x075A): (chr(0x062F), 0),  # Dal with inverted small V below
    chr(0x08AE): (chr(0x062F), 3),  # Dal with three dots above
    # Reh
    chr(0x0631): (chr(0x0631), 0),  # Reh
    chr(0x0632): (chr(0x0631), 1),  # Zain
    chr(0x0691): (chr(0x0631), 0),  # Rreh (Reh with small tah)
    chr(0x0692): (chr(0x0631), 0),  # Reh with small V
    chr(0x0693): (chr(0x0631), 0),  # Reh with ring
    chr(0x0694): (chr(0x0631), 1),  # Reh with dot below
    chr(0x0695): (chr(0x0631), 0),  # Reh with small V below
    chr(0x0696): (chr(0x0631), 2),  # Reh with dot below and dot above
    chr(0x0697): (chr(0x0631), 2),  # Reh with two dots above
    chr(0x0698): (chr(0x0631), 3),  # Jeh (Reh with three dots above)
    chr(0x0699): (chr(0x0631), 4),  # Reh with four dots above
    chr(0x06EF): (chr(0x0631), 0),  # Reh with inverted V (above)
    chr(0x075B): (chr(0x0631), 0),  # Reh with stroke
    chr(0x076B): (chr(0x0631), 2),  # Reh with two dots vertically above
    chr(0x076C): (chr(0x0631), 0),  # Reh with hamza above
    chr(0x0771): (chr(0x0631), 2),  # Reh with two dots and tah above
    chr(0x08B2): (chr(0x0631), 1),  # Zain with inverted v above
    chr(0x08B9): (chr(0x0631), 1),  # Reh with small noon above
    # Rohingya Yeh
    chr(0x08AA): (chr(0x0631), 0),  # Reh with loop in the end
    # Seen
    chr(0x0633): (chr(0x0633), 0),  # Seen
    chr(0x0634): (chr(0x0633), 3),  # Sheen
    chr(0x069A): (chr(0x0633), 2),  # Seen with dot below and dot above
    chr(0x069B): (chr(0x0633), 3),  # Seen with three dots below
    chr(0x069C): (chr(0x0633), 6),  # Seen with three dots below and three dots above
    chr(0x06FA): (chr(0x0633), 4),  # Sheen with dot below
    chr(0x075C): (chr(0x0633), 4),  # Seen with four dots above
    chr(0x076D): (chr(0x0633), 2),  # Seen with two dots vertically above
    chr(0x0770): (chr(0x0633), 2),  # Seen with two dots and tah above
    chr(0x077D): (chr(0x0633), 0),  # Seen with four above
    chr(0x077E): (chr(0x0633), 0),  # Seen with inverted V above
    # Sad
    chr(0x0635): (chr(0x0635), 0),  # Sad
    chr(0x0636): (chr(0x0635), 1),  # Dad
    chr(0x069D): (chr(0x0635), 2),  # Sad with two dots below
    chr(0x069E): (chr(0x0635), 3),  # Sad with three dots above
    chr(0x06FB): (chr(0x0635), 2),  # Dad with dot below
    chr(0x08AF): (chr(0x0635), 3),  # Sad with three dots below
    # Tah
    chr(0x0637): (chr(0x0637), 0),  # Tah
    chr(0x0638): (chr(0x0637), 1),  # Zah (Tah with dot above)
    chr(0x069F): (chr(0x0637), 3),  # Tah with three dots above
    chr(0x08A3): (chr(0x0637), 2),  # Tah with two dots above
    # Ain
    chr(0x0639): (chr(0x0639), 0),  # Ain
    chr(0x063A): (chr(0x0639), 1),  # Ghain
    chr(0x06A0): (chr(0x0639), 3),  # Ain with three dots above
    chr(0x06FC): (chr(0x0639), 2),  # Ghain with dot below
    chr(0x075D): (chr(0x0639), 2),  # Ain with two dots above (horizontal)
    chr(0x075E): (chr(0x0639), 3),  # Ain with three dots pointing downwards above
    chr(0x075F): (chr(0x0639), 2),  # Ain with two dots vertically above
    chr(0x08B3): (chr(0x0639), 3),  # Ain with three dots below
    # Feh
    chr(0x0641): (chr(0x06A1), 1),  # Feh
    chr(0x06A1): (chr(0x06A1), 0),  # Dotless feh
    chr(0x06A2): (chr(0x06A1), 1),  # Feh with dot moved below
    chr(0x06A3): (chr(0x06A1), 2),  # Feh with dot below
    chr(0x06A4): (chr(0x06A1), 3),  # Veh (Feh with there dots above)
    chr(0x06A5): (chr(0x06A1), 3),  # Feh with three dots below
    chr(0x06A6): (chr(0x06A1), 4),  # Peheh (Feh with four dots above)
    chr(0x0760): (chr(0x06A1), 2),  # Feh with two dots below (horizontal)
    chr(0x0761): (chr(0x06A1), 3),  # Feh with three dots pointing upwards below
    chr(0x08A4): (chr(0x06A1), 4),  # Dotless feh with dot below and three dots above
    chr(0x08BB): (chr(0x06A1), (0, 1)),  # African Feh
                                         # dotless: initial and medial forms have one dot below
    # Qaf
    chr(0x0642): (chr(0x066F), 2),  # Qaf
    chr(0x066F): (chr(0x066F), 0),  # Dotless qaf
    chr(0x06A7): (chr(0x066F), 1),  # Qaf with dot above
    chr(0x06A8): (chr(0x066F), 3),  # Qaf with three dots above
    chr(0x08A5): (chr(0x066F), 3),  # Qaf with dot below
    chr(0x08BC): (chr(0x066F), (0, 1)),  # African Qaf
                                         # dotless: initial and medial forms have one dot above
    # Kaf
    chr(0x0643): (chr(0x0643), 0),  # Kaf
    chr(0x06AC): (chr(0x0643), 1),  # Kaf with dot above
    chr(0x06AD): (chr(0x0643), 3),  # Ng (Kaf with three dots above)
    chr(0x06AE): (chr(0x0643), 3),  # Kaf with three dots below
    chr(0x077F): (chr(0x0643), 2),  # Kaf with two dots above
    chr(0x08B4): (chr(0x0643), 1),  # Kaf with dot below
    # Farsi Kaf
    chr(0x063B): (chr(0x06A9), 2),  # Keheh with two dots above
    chr(0x063C): (chr(0x06A9), 3),  # Keheh with three dots below
    chr(0x06A9): (chr(0x06A9), 0),  # Keheh (Urdu kaf)
    chr(0x06AB): (chr(0x06A9), 0),  # Kaf with ring
    chr(0x0762): (chr(0x06A9), 1),  # Keheh with dot above
    chr(0x0763): (chr(0x06A9), 3),  # Keheh with three dots above (pointing upwards)
    chr(0x0764): (chr(0x06A9), 3),  # Keheh with three dots poiting upwards below
    # Sindhi Kaf
    chr(0x06AA): (chr(0x06AA), 0),  # Swash kaf
    # Gaf
    chr(0x06AF): (chr(0x06AF), 0),  # Gaf
    chr(0x06B0): (chr(0x06AF), 0),  # Gaf with ring
    chr(0x06B1): (chr(0x06AF), 2),  # Ngoeh (Gaf with two dots above)
    chr(0x06B2): (chr(0x06AF), 2),  # Gaf with two dots below
    chr(0x06B3): (chr(0x06AF), 2),  # Gueh (Gaf with two dots vertically below)
    chr(0x06B4): (chr(0x06AF), 3),  # Gaf with three dots above
    # Gaf with inverted stroke
    chr(0x08B0): (chr(0x08B0), 0),  # Gaf with inverted stroke
    # Lam
    chr(0x0644): (chr(0x0644), 0),  # Lam
    chr(0x06B5): (chr(0x0644), 0),  # Lam with small V
    chr(0x06B6): (chr(0x0644), 1),  # Lam with dot above
    chr(0x06B7): (chr(0x0644), 3),  # Lam with three dots above
    chr(0x06B8): (chr(0x0644), 3),  # Lam with three dots below
    chr(0x076A): (chr(0x0644), 0),  # Lam with bar (in the middle)
    chr(0x08A6): (chr(0x0644), 0),  # Lam with two bars (in the middle)
    # Meem
    chr(0x0645): (chr(0x0645), 0),  # Meem
    chr(0x06FE): (chr(0x0645), 0),  # Sindhi postposition men
    chr(0x0765): (chr(0x0645), 1),  # Meem with dot above
    chr(0x0766): (chr(0x0645), 1),  # Meem with dot below
    chr(0x08A7): (chr(0x0645), 3),  # Meem with three dots above
    # Noon
    chr(0x0646): (chr(0x06BA), 1),  # Noon
    chr(0x06B9): (chr(0x06BA), 2),  # Noon with dot below
    chr(0x06BA): (chr(0x06BA), 0),  # Noon ghunna
    chr(0x06BB): (chr(0x06BA), 0),  # Rhoon (Dotless noon with small tah above)
    chr(0x06BC): (chr(0x06BA), 1),  # Noon with ring
    chr(0x06BD): (chr(0x06BA), 3),  # Noon with three dots above
    chr(0x0767): (chr(0x06BA), 3),  # Noon with two dots below
    chr(0x0768): (chr(0x06BA), 1),  # Noon with small tah (above)
    chr(0x0769): (chr(0x06BA), 1),  # Noon with small V (above)
    chr(0x08BD): (chr(0x06BA), (0, 1)),  # African Noon
                                         # Dotless: initial and medial forms have one dot above
    # Heh
    chr(0x0647): (chr(0x0647), 0),  # Heh
    # Heh Dochashmi
    chr(0x06BE): (chr(0x06BE), 0),  # Heh Doachashmee
    chr(0x06FF): (chr(0x06BE), 0),  # Heh with inverted V
    # Heh Goal
    chr(0x06C1): (chr(0x06C1), 0),  # Heh Goal
    chr(0x06C2): (chr(0x06C1), 0),  # Heh goal with hamza above
    # Waw
    chr(0x0648): (chr(0x0648), 0),  # High hamza alef
    chr(0x0676): (chr(0x0648), 0),  # High hamza waw
    chr(0x0677): (chr(0x0648), 0),  # U with hamza above
    chr(0x06C4): (chr(0x0648), 0),  # Waw with ring
    chr(0x06C5): (chr(0x0648), 0),  # Kirghiz Oe (Waw with stroke in the middle)
    chr(0x06C6): (chr(0x0648), 0),  # Oe (Waw with small V above)
    chr(0x06C7): (chr(0x0648), 0),  # U (Waw with damma above)
    chr(0x06C8): (chr(0x0648), 0),  # Yu (Waw with vertical bar above)
    chr(0x06C9): (chr(0x0648), 0),  # Kirghiz Yu (Waw with inverted V above)
    chr(0x06CA): (chr(0x0648), 2),  # Waw with two dots above
    chr(0x06CB): (chr(0x0648), 3),  # Ve (Waw with three dots above)
    chr(0x06CF): (chr(0x0648), 1),  # Waw with dot above
    chr(0x0778): (chr(0x0648), 0),  # Waw with two above
    chr(0x0779): (chr(0x0648), 0),  # Waw with three above
    chr(0x08AB): (chr(0x0648), 1),  # Waw with dot within
    chr(0x08B1): (chr(0x08B1), 0),  # Straight waw
    # Yeh
    chr(0x063D): (chr(0x0649), (0, 2)),  # Farsi yeh with inverted V
    chr(0x063E): (chr(0x0649), (2, 4)),  # Farsi yeh with two dots above
    chr(0x063F): (chr(0x0649), (3, 5)),  # Farsi yeh with three dots above
    chr(0x0649): (chr(0x0649), 0),  # Alef maqsura
    chr(0x064A): (chr(0x0649), 2),  # Yeh
    chr(0x0678): (chr(0x0649), 0),  # High hamza yeh
    chr(0x06CC): (chr(0x0649), (0, 2)),  # Farsi Yeh
    chr(0x06CD): (chr(0x0649), 0),  # Yeh with tail
    chr(0x06CE): (chr(0x0649), (0, 2)),  # Yeh with small V (without dots)
    chr(0x06D0): (chr(0x0649), 2),  # E (yeh with two dots vertically below)
    chr(0x06D1): (chr(0x0649), 3),  # Yeh with three dots below
    chr(0x0775): (chr(0x0649), 0),  # Yeh with two above
    chr(0x0776): (chr(0x0649), 0),  # Yeh with three above
    chr(0x0777): (chr(0x0649), 0),  # Yeh with four below
    chr(0x08A8): (chr(0x0649), 2),  # Yeh with two dots below and hamza above
    chr(0x08A9): (chr(0x0649), 3),  # Dotted Yeh with dot above
    chr(0x08BA): (chr(0x0649), 3),  # Dotted Yeh with small noon above
    # Yeh Barree
    chr(0x06D2): (chr(0x06D2), 0),  # Yeh Barree
    chr(0x06D3): (chr(0x06D2), 0),  # Yeh Barree with hamza above
    chr(0x077A): (chr(0x06D2), 0),  # Yeh Barree with two above
    chr(0x077B): (chr(0x06D2), 0),  # Yeh Barree with three above
    # Rohingya Yeh
    chr(0x08AC): (chr(0x08AC), 2),  # Rohingya Yeh (no dotless alternative )
}

def get_base_form(c):
    return base_form[c]
