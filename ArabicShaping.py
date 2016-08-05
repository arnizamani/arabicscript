from JoiningGroup import JoiningType, JoiningGroup

joining_groups = {
    0x0600: JoiningGroup.No_Joining_Group,
    0x0601: JoiningGroup.No_Joining_Group,
    0x0602: JoiningGroup.No_Joining_Group,
    0x0603: JoiningGroup.No_Joining_Group,
    0x0604: JoiningGroup.No_Joining_Group,
    0x0605: JoiningGroup.No_Joining_Group,
    0x0608: JoiningGroup.No_Joining_Group,
    0x060B: JoiningGroup.No_Joining_Group,
    0x0620: JoiningGroup.Yeh,
    0x0621: JoiningGroup.No_Joining_Group,
    0x0622: JoiningGroup.Alef,
    0x0623: JoiningGroup.Alef,
    0x0624: JoiningGroup.Waw,
    0x0625: JoiningGroup.Alef,
    0x0626: JoiningGroup.Yeh,
    0x0627: JoiningGroup.Alef,
    0x0628: JoiningGroup.Beh,
    0x0629: JoiningGroup.Teh_Marbuta,
    0x062A: JoiningGroup.Beh,
    0x062B: JoiningGroup.Beh,
    0x062C: JoiningGroup.Hah,
    0x062D: JoiningGroup.Hah,
    0x062E: JoiningGroup.Hah,
    0x062F: JoiningGroup.Dal,
    0x0630: JoiningGroup.Dal,
    0x0631: JoiningGroup.Reh,
    0x0632: JoiningGroup.Reh,
    0x0633: JoiningGroup.Seen,
    0x0634: JoiningGroup.Seen,
    0x0635: JoiningGroup.Sad,
    0x0636: JoiningGroup.Sad,
    0x0637: JoiningGroup.Tah,
    0x0638: JoiningGroup.Tah,
    0x0639: JoiningGroup.Ain,
    0x063A: JoiningGroup.Ain,
    0x063B: JoiningGroup.Gaf,
    0x063C: JoiningGroup.Gaf,
    0x063D: JoiningGroup.Farsi_Yeh,
    0x063E: JoiningGroup.Farsi_Yeh,
    0x063F: JoiningGroup.Farsi_Yeh,
    0x0640: JoiningGroup.No_Joining_Group,
    0x0641: JoiningGroup.Feh,
    0x0642: JoiningGroup.Qaf,
    0x0643: JoiningGroup.Kaf,
    0x0644: JoiningGroup.Lam,
    0x0645: JoiningGroup.Meem,
    0x0646: JoiningGroup.Noon,
    0x0647: JoiningGroup.Heh,
    0x0648: JoiningGroup.Waw,
    0x0649: JoiningGroup.Yeh,
    0x064A: JoiningGroup.Yeh,
    0x066E: JoiningGroup.Beh,
    0x066F: JoiningGroup.Qaf,
    0x0671: JoiningGroup.Alef,
    0x0672: JoiningGroup.Alef,
    0x0673: JoiningGroup.Alef,
    0x0674: JoiningGroup.No_Joining_Group,
    0x0675: JoiningGroup.Alef,
    0x0676: JoiningGroup.Waw,
    0x0677: JoiningGroup.Waw,
    0x0678: JoiningGroup.Yeh,
    0x0679: JoiningGroup.Beh,
    0x067A: JoiningGroup.Beh,
    0x067B: JoiningGroup.Beh,
    0x067C: JoiningGroup.Beh,
    0x067D: JoiningGroup.Beh,
    0x067E: JoiningGroup.Beh,
    0x067F: JoiningGroup.Beh,
    0x0680: JoiningGroup.Beh,
    0x0681: JoiningGroup.Hah,
    0x0682: JoiningGroup.Hah,
    0x0683: JoiningGroup.Hah,
    0x0684: JoiningGroup.Hah,
    0x0685: JoiningGroup.Hah,
    0x0686: JoiningGroup.Hah,
    0x0687: JoiningGroup.Hah,
    0x0688: JoiningGroup.Dal,
    0x0689: JoiningGroup.Dal,
    0x068A: JoiningGroup.Dal,
    0x068B: JoiningGroup.Dal,
    0x068C: JoiningGroup.Dal,
    0x068D: JoiningGroup.Dal,
    0x068E: JoiningGroup.Dal,
    0x068F: JoiningGroup.Dal,
    0x0690: JoiningGroup.Dal,
    0x0691: JoiningGroup.Reh,
    0x0692: JoiningGroup.Reh,
    0x0693: JoiningGroup.Reh,
    0x0694: JoiningGroup.Reh,
    0x0695: JoiningGroup.Reh,
    0x0696: JoiningGroup.Reh,
    0x0697: JoiningGroup.Reh,
    0x0698: JoiningGroup.Reh,
    0x0699: JoiningGroup.Reh,
    0x069A: JoiningGroup.Seen,
    0x069B: JoiningGroup.Seen,
    0x069C: JoiningGroup.Seen,
    0x069D: JoiningGroup.Sad,
    0x069E: JoiningGroup.Sad,
    0x069F: JoiningGroup.Tah,
    0x06A0: JoiningGroup.Ain,
    0x06A1: JoiningGroup.Feh,
    0x06A2: JoiningGroup.Feh,
    0x06A3: JoiningGroup.Feh,
    0x06A4: JoiningGroup.Feh,
    0x06A5: JoiningGroup.Feh,
    0x06A6: JoiningGroup.Feh,
    0x06A7: JoiningGroup.Qaf,
    0x06A8: JoiningGroup.Qaf,
    0x06A9: JoiningGroup.Gaf,
    0x06AA: JoiningGroup.Swash_Kaf,
    0x06AB: JoiningGroup.Gaf,
    0x06AC: JoiningGroup.Kaf,
    0x06AD: JoiningGroup.Kaf,
    0x06AE: JoiningGroup.Kaf,
    0x06AF: JoiningGroup.Gaf,
    0x06B0: JoiningGroup.Gaf,
    0x06B1: JoiningGroup.Gaf,
    0x06B2: JoiningGroup.Gaf,
    0x06B3: JoiningGroup.Gaf,
    0x06B4: JoiningGroup.Gaf,
    0x06B5: JoiningGroup.Lam,
    0x06B6: JoiningGroup.Lam,
    0x06B7: JoiningGroup.Lam,
    0x06B8: JoiningGroup.Lam,
    0x06B9: JoiningGroup.Noon,
    0x06BA: JoiningGroup.Noon,
    0x06BB: JoiningGroup.Noon,
    0x06BC: JoiningGroup.Noon,
    0x06BD: JoiningGroup.Nya,
    0x06BE: JoiningGroup.Knotted_Heh,
    0x06BF: JoiningGroup.Hah,
    0x06C0: JoiningGroup.Teh_Marbuta,
    0x06C1: JoiningGroup.Heh_Goal,
    0x06C2: JoiningGroup.Heh_Goal,
    0x06C3: JoiningGroup.Teh_Marbuta_Goal,
    0x06C4: JoiningGroup.Waw,
    0x06C5: JoiningGroup.Waw,
    0x06C6: JoiningGroup.Waw,
    0x06C7: JoiningGroup.Waw,
    0x06C8: JoiningGroup.Waw,
    0x06C9: JoiningGroup.Waw,
    0x06CA: JoiningGroup.Waw,
    0x06CB: JoiningGroup.Waw,
    0x06CC: JoiningGroup.Farsi_Yeh,
    0x06CD: JoiningGroup.Yeh_With_Tail,
    0x06CE: JoiningGroup.Farsi_Yeh,
    0x06CF: JoiningGroup.Waw,
    0x06D0: JoiningGroup.Yeh,
    0x06D1: JoiningGroup.Yeh,
    0x06D2: JoiningGroup.Yeh_Barree,
    0x06D3: JoiningGroup.Yeh_Barree,
    0x06D5: JoiningGroup.Teh_Marbuta,
    0x06DD: JoiningGroup.No_Joining_Group,
    0x06EE: JoiningGroup.Dal,
    0x06EF: JoiningGroup.Reh,
    0x06FA: JoiningGroup.Seen,
    0x06FB: JoiningGroup.Sad,
    0x06FC: JoiningGroup.Ain,
    0x06FF: JoiningGroup.Knotted_Heh,
    0x0750: JoiningGroup.Beh,
    0x0751: JoiningGroup.Beh,
    0x0752: JoiningGroup.Beh,
    0x0753: JoiningGroup.Beh,
    0x0754: JoiningGroup.Beh,
    0x0755: JoiningGroup.Beh,
    0x0756: JoiningGroup.Beh,
    0x0757: JoiningGroup.Hah,
    0x0758: JoiningGroup.Hah,
    0x0759: JoiningGroup.Dal,
    0x075A: JoiningGroup.Dal,
    0x075B: JoiningGroup.Reh,
    0x075C: JoiningGroup.Seen,
    0x075D: JoiningGroup.Ain,
    0x075E: JoiningGroup.Ain,
    0x075F: JoiningGroup.Ain,
    0x0760: JoiningGroup.Feh,
    0x0761: JoiningGroup.Feh,
    0x0762: JoiningGroup.Gaf,
    0x0763: JoiningGroup.Gaf,
    0x0764: JoiningGroup.Gaf,
    0x0765: JoiningGroup.Meem,
    0x0766: JoiningGroup.Meem,
    0x0767: JoiningGroup.Noon,
    0x0768: JoiningGroup.Noon,
    0x0769: JoiningGroup.Noon,
    0x076A: JoiningGroup.Lam,
    0x076B: JoiningGroup.Reh,
    0x076C: JoiningGroup.Reh,
    0x076D: JoiningGroup.Seen,
    0x076E: JoiningGroup.Hah,
    0x076F: JoiningGroup.Hah,
    0x0770: JoiningGroup.Seen,
    0x0771: JoiningGroup.Reh,
    0x0772: JoiningGroup.Hah,
    0x0773: JoiningGroup.Alef,
    0x0774: JoiningGroup.Alef,
    0x0775: JoiningGroup.Farsi_Yeh,
    0x0776: JoiningGroup.Farsi_Yeh,
    0x0777: JoiningGroup.Yeh,
    0x0778: JoiningGroup.Waw,
    0x0779: JoiningGroup.Waw,
    0x077A: JoiningGroup.Burushaski_Yeh_Barree,
    0x077B: JoiningGroup.Burushaski_Yeh_Barree,
    0x077C: JoiningGroup.Hah,
    0x077D: JoiningGroup.Seen,
    0x077E: JoiningGroup.Seen,
    0x077F: JoiningGroup.Kaf,
    0x08A0: JoiningGroup.Beh,
    0x08A1: JoiningGroup.Beh,
    0x08A2: JoiningGroup.Hah,
    0x08A3: JoiningGroup.Tah,
    0x08A4: JoiningGroup.Feh,
    0x08A5: JoiningGroup.Qaf,
    0x08A6: JoiningGroup.Lam,
    0x08A7: JoiningGroup.Meem,
    0x08A8: JoiningGroup.Yeh,
    0x08A9: JoiningGroup.Yeh,
    0x08AA: JoiningGroup.Reh,
    0x08AB: JoiningGroup.Waw,
    0x08AC: JoiningGroup.Rohingya_Yeh,
    0x08AD: JoiningGroup.No_Joining_Group,
    0x08AE: JoiningGroup.Dal,
    0x08AF: JoiningGroup.Sad,
    0x08B0: JoiningGroup.Gaf,
    0x08B1: JoiningGroup.Straight_Waw,
    0x08B2: JoiningGroup.Reh,
    0x08B3: JoiningGroup.Ain,
    0x08B4: JoiningGroup.Kaf,
    0x08B6: JoiningGroup.Beh,
    0x08B7: JoiningGroup.Beh,
    0x08B8: JoiningGroup.Beh,
    0x08B9: JoiningGroup.Reh,
    0x08BA: JoiningGroup.Yeh,
    0x08BB: JoiningGroup.African_Feh,
    0x08BC: JoiningGroup.African_Qaf,
    0x08BD: JoiningGroup.African_Noon,
    0x08E2: JoiningGroup.No_Joining_Group,
}
joining_types = {
    0x0600: JoiningType.Non_Joining,
    0x0601: JoiningType.Non_Joining,
    0x0602: JoiningType.Non_Joining,
    0x0603: JoiningType.Non_Joining,
    0x0604: JoiningType.Non_Joining,
    0x0605: JoiningType.Non_Joining,
    0x0608: JoiningType.Non_Joining,
    0x060B: JoiningType.Non_Joining,
    0x0620: JoiningType.Dual_Joining,
    0x0621: JoiningType.Non_Joining,
    0x0622: JoiningType.Right_Joining,
    0x0623: JoiningType.Right_Joining,
    0x0624: JoiningType.Right_Joining,
    0x0625: JoiningType.Right_Joining,
    0x0626: JoiningType.Dual_Joining,
    0x0627: JoiningType.Right_Joining,
    0x0628: JoiningType.Dual_Joining,
    0x0629: JoiningType.Right_Joining,
    0x062A: JoiningType.Dual_Joining,
    0x062B: JoiningType.Dual_Joining,
    0x062C: JoiningType.Dual_Joining,
    0x062D: JoiningType.Dual_Joining,
    0x062E: JoiningType.Dual_Joining,
    0x062F: JoiningType.Right_Joining,
    0x0630: JoiningType.Right_Joining,
    0x0631: JoiningType.Right_Joining,
    0x0632: JoiningType.Right_Joining,
    0x0633: JoiningType.Dual_Joining,
    0x0634: JoiningType.Dual_Joining,
    0x0635: JoiningType.Dual_Joining,
    0x0636: JoiningType.Dual_Joining,
    0x0637: JoiningType.Dual_Joining,
    0x0638: JoiningType.Dual_Joining,
    0x0639: JoiningType.Dual_Joining,
    0x063A: JoiningType.Dual_Joining,
    0x063B: JoiningType.Dual_Joining,
    0x063C: JoiningType.Dual_Joining,
    0x063D: JoiningType.Dual_Joining,
    0x063E: JoiningType.Dual_Joining,
    0x063F: JoiningType.Dual_Joining,
    0x0640: JoiningType.Join_Causing,
    0x0641: JoiningType.Dual_Joining,
    0x0642: JoiningType.Dual_Joining,
    0x0643: JoiningType.Dual_Joining,
    0x0644: JoiningType.Dual_Joining,
    0x0645: JoiningType.Dual_Joining,
    0x0646: JoiningType.Dual_Joining,
    0x0647: JoiningType.Dual_Joining,
    0x0648: JoiningType.Right_Joining,
    0x0649: JoiningType.Dual_Joining,
    0x064A: JoiningType.Dual_Joining,
    0x066E: JoiningType.Dual_Joining,
    0x066F: JoiningType.Dual_Joining,
    0x0671: JoiningType.Right_Joining,
    0x0672: JoiningType.Right_Joining,
    0x0673: JoiningType.Right_Joining,
    0x0674: JoiningType.Non_Joining,
    0x0675: JoiningType.Right_Joining,
    0x0676: JoiningType.Right_Joining,
    0x0677: JoiningType.Right_Joining,
    0x0678: JoiningType.Dual_Joining,
    0x0679: JoiningType.Dual_Joining,
    0x067A: JoiningType.Dual_Joining,
    0x067B: JoiningType.Dual_Joining,
    0x067C: JoiningType.Dual_Joining,
    0x067D: JoiningType.Dual_Joining,
    0x067E: JoiningType.Dual_Joining,
    0x067F: JoiningType.Dual_Joining,
    0x0680: JoiningType.Dual_Joining,
    0x0681: JoiningType.Dual_Joining,
    0x0682: JoiningType.Dual_Joining,
    0x0683: JoiningType.Dual_Joining,
    0x0684: JoiningType.Dual_Joining,
    0x0685: JoiningType.Dual_Joining,
    0x0686: JoiningType.Dual_Joining,
    0x0687: JoiningType.Dual_Joining,
    0x0688: JoiningType.Right_Joining,
    0x0689: JoiningType.Right_Joining,
    0x068A: JoiningType.Right_Joining,
    0x068B: JoiningType.Right_Joining,
    0x068C: JoiningType.Right_Joining,
    0x068D: JoiningType.Right_Joining,
    0x068E: JoiningType.Right_Joining,
    0x068F: JoiningType.Right_Joining,
    0x0690: JoiningType.Right_Joining,
    0x0691: JoiningType.Right_Joining,
    0x0692: JoiningType.Right_Joining,
    0x0693: JoiningType.Right_Joining,
    0x0694: JoiningType.Right_Joining,
    0x0695: JoiningType.Right_Joining,
    0x0696: JoiningType.Right_Joining,
    0x0697: JoiningType.Right_Joining,
    0x0698: JoiningType.Right_Joining,
    0x0699: JoiningType.Right_Joining,
    0x069A: JoiningType.Dual_Joining,
    0x069B: JoiningType.Dual_Joining,
    0x069C: JoiningType.Dual_Joining,
    0x069D: JoiningType.Dual_Joining,
    0x069E: JoiningType.Dual_Joining,
    0x069F: JoiningType.Dual_Joining,
    0x06A0: JoiningType.Dual_Joining,
    0x06A1: JoiningType.Dual_Joining,
    0x06A2: JoiningType.Dual_Joining,
    0x06A3: JoiningType.Dual_Joining,
    0x06A4: JoiningType.Dual_Joining,
    0x06A5: JoiningType.Dual_Joining,
    0x06A6: JoiningType.Dual_Joining,
    0x06A7: JoiningType.Dual_Joining,
    0x06A8: JoiningType.Dual_Joining,
    0x06A9: JoiningType.Dual_Joining,
    0x06AA: JoiningType.Dual_Joining,
    0x06AB: JoiningType.Dual_Joining,
    0x06AC: JoiningType.Dual_Joining,
    0x06AD: JoiningType.Dual_Joining,
    0x06AE: JoiningType.Dual_Joining,
    0x06AF: JoiningType.Dual_Joining,
    0x06B0: JoiningType.Dual_Joining,
    0x06B1: JoiningType.Dual_Joining,
    0x06B2: JoiningType.Dual_Joining,
    0x06B3: JoiningType.Dual_Joining,
    0x06B4: JoiningType.Dual_Joining,
    0x06B5: JoiningType.Dual_Joining,
    0x06B6: JoiningType.Dual_Joining,
    0x06B7: JoiningType.Dual_Joining,
    0x06B8: JoiningType.Dual_Joining,
    0x06B9: JoiningType.Dual_Joining,
    0x06BA: JoiningType.Dual_Joining,
    0x06BB: JoiningType.Dual_Joining,
    0x06BC: JoiningType.Dual_Joining,
    0x06BD: JoiningType.Dual_Joining,
    0x06BE: JoiningType.Dual_Joining,
    0x06BF: JoiningType.Dual_Joining,
    0x06C0: JoiningType.Right_Joining,
    0x06C1: JoiningType.Dual_Joining,
    0x06C2: JoiningType.Dual_Joining,
    0x06C3: JoiningType.Right_Joining,
    0x06C4: JoiningType.Right_Joining,
    0x06C5: JoiningType.Right_Joining,
    0x06C6: JoiningType.Right_Joining,
    0x06C7: JoiningType.Right_Joining,
    0x06C8: JoiningType.Right_Joining,
    0x06C9: JoiningType.Right_Joining,
    0x06CA: JoiningType.Right_Joining,
    0x06CB: JoiningType.Right_Joining,
    0x06CC: JoiningType.Dual_Joining,
    0x06CD: JoiningType.Right_Joining,
    0x06CE: JoiningType.Dual_Joining,
    0x06CF: JoiningType.Right_Joining,
    0x06D0: JoiningType.Dual_Joining,
    0x06D1: JoiningType.Dual_Joining,
    0x06D2: JoiningType.Right_Joining,
    0x06D3: JoiningType.Right_Joining,
    0x06D5: JoiningType.Right_Joining,
    0x06DD: JoiningType.Non_Joining,
    0x06EE: JoiningType.Right_Joining,
    0x06EF: JoiningType.Right_Joining,
    0x06FA: JoiningType.Dual_Joining,
    0x06FB: JoiningType.Dual_Joining,
    0x06FC: JoiningType.Dual_Joining,
    0x06FF: JoiningType.Dual_Joining,
    0x0750: JoiningType.Dual_Joining,
    0x0751: JoiningType.Dual_Joining,
    0x0752: JoiningType.Dual_Joining,
    0x0753: JoiningType.Dual_Joining,
    0x0754: JoiningType.Dual_Joining,
    0x0755: JoiningType.Dual_Joining,
    0x0756: JoiningType.Dual_Joining,
    0x0757: JoiningType.Dual_Joining,
    0x0758: JoiningType.Dual_Joining,
    0x0759: JoiningType.Right_Joining,
    0x075A: JoiningType.Right_Joining,
    0x075B: JoiningType.Right_Joining,
    0x075C: JoiningType.Dual_Joining,
    0x075D: JoiningType.Dual_Joining,
    0x075E: JoiningType.Dual_Joining,
    0x075F: JoiningType.Dual_Joining,
    0x0760: JoiningType.Dual_Joining,
    0x0761: JoiningType.Dual_Joining,
    0x0762: JoiningType.Dual_Joining,
    0x0763: JoiningType.Dual_Joining,
    0x0764: JoiningType.Dual_Joining,
    0x0765: JoiningType.Dual_Joining,
    0x0766: JoiningType.Dual_Joining,
    0x0767: JoiningType.Dual_Joining,
    0x0768: JoiningType.Dual_Joining,
    0x0769: JoiningType.Dual_Joining,
    0x076A: JoiningType.Dual_Joining,
    0x076B: JoiningType.Right_Joining,
    0x076C: JoiningType.Right_Joining,
    0x076D: JoiningType.Dual_Joining,
    0x076E: JoiningType.Dual_Joining,
    0x076F: JoiningType.Dual_Joining,
    0x0770: JoiningType.Dual_Joining,
    0x0771: JoiningType.Right_Joining,
    0x0772: JoiningType.Dual_Joining,
    0x0773: JoiningType.Right_Joining,
    0x0774: JoiningType.Right_Joining,
    0x0775: JoiningType.Dual_Joining,
    0x0776: JoiningType.Dual_Joining,
    0x0777: JoiningType.Dual_Joining,
    0x0778: JoiningType.Right_Joining,
    0x0779: JoiningType.Right_Joining,
    0x077A: JoiningType.Dual_Joining,
    0x077B: JoiningType.Dual_Joining,
    0x077C: JoiningType.Dual_Joining,
    0x077D: JoiningType.Dual_Joining,
    0x077E: JoiningType.Dual_Joining,
    0x077F: JoiningType.Dual_Joining,
    0x08A0: JoiningType.Dual_Joining,
    0x08A1: JoiningType.Dual_Joining,
    0x08A2: JoiningType.Dual_Joining,
    0x08A3: JoiningType.Dual_Joining,
    0x08A4: JoiningType.Dual_Joining,
    0x08A5: JoiningType.Dual_Joining,
    0x08A6: JoiningType.Dual_Joining,
    0x08A7: JoiningType.Dual_Joining,
    0x08A8: JoiningType.Dual_Joining,
    0x08A9: JoiningType.Dual_Joining,
    0x08AA: JoiningType.Right_Joining,
    0x08AB: JoiningType.Right_Joining,
    0x08AC: JoiningType.Right_Joining,
    0x08AD: JoiningType.Non_Joining,
    0x08AE: JoiningType.Right_Joining,
    0x08AF: JoiningType.Dual_Joining,
    0x08B0: JoiningType.Dual_Joining,
    0x08B1: JoiningType.Right_Joining,
    0x08B2: JoiningType.Right_Joining,
    0x08B3: JoiningType.Dual_Joining,
    0x08B4: JoiningType.Dual_Joining,
    0x08B6: JoiningType.Dual_Joining,
    0x08B7: JoiningType.Dual_Joining,
    0x08B8: JoiningType.Dual_Joining,
    0x08B9: JoiningType.Right_Joining,
    0x08BA: JoiningType.Dual_Joining,
    0x08BB: JoiningType.Dual_Joining,
    0x08BC: JoiningType.Dual_Joining,
    0x08BD: JoiningType.Dual_Joining,
    0x08E2: JoiningType.Non_Joining,
}
