object Form1: TForm1
  Left = 270
  Top = 146
  BorderStyle = bsNone
  Caption = #1043#1083#1072#1074#1085#1072#1103' '#1092#1086#1088#1084#1072
  ClientHeight = 398
  ClientWidth = 806
  Color = clActiveCaption
  Font.Charset = RUSSIAN_CHARSET
  Font.Color = clBlack
  Font.Height = -16
  Font.Name = 'Calibri'
  Font.Style = []
  OldCreateOrder = False
  Position = poScreenCenter
  OnCreate = FormCreate
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 19
  object Label1: TLabel
    Left = 447
    Top = 322
    Width = 116
    Height = 15
    Caption = #1050#1086#1083#1080#1095#1077#1089#1090#1074#1086' '#1087#1086#1090#1086#1082#1086#1074':'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clBlack
    Font.Height = -13
    Font.Name = 'Calibri'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Label2: TLabel
    Left = 589
    Top = 320
    Width = 8
    Height = 19
    Caption = '0'
    Font.Charset = ANSI_CHARSET
    Font.Color = clBlack
    Font.Height = -16
    Font.Name = 'Calibri'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object lbl4: TLabel
    Left = 768
    Top = 319
    Width = 8
    Height = 19
    Caption = '1'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clBlack
    Font.Height = -16
    Font.Name = 'Calibri'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Label3: TLabel
    Left = 34
    Top = 318
    Width = 107
    Height = 19
    Caption = #1082#1086#1083'-'#1074#1086' '#1092#1072#1081#1083#1086#1074' :'
  end
  object Label4: TLabel
    Left = 1056
    Top = 560
    Width = 43
    Height = 19
    Caption = 'Label4'
    Visible = False
  end
  object Button1: TButton
    Left = 563
    Top = 54
    Width = 95
    Height = 33
    Caption = #1047#1072#1087#1091#1089#1082
    Enabled = False
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clGray
    Font.Height = -16
    Font.Name = 'Arial Narrow'
    Font.Style = []
    ParentFont = False
    TabOrder = 0
    OnClick = Button1Click
  end
  object Memo1: TMemo
    Left = 34
    Top = 102
    Width = 409
    Height = 201
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clGray
    Font.Height = -16
    Font.Name = 'Arial Narrow'
    Font.Style = []
    ParentFont = False
    ScrollBars = ssVertical
    TabOrder = 1
  end
  object Button3: TButton
    Left = 458
    Top = 54
    Width = 97
    Height = 33
    Caption = #1054#1090#1082#1088#1099#1090#1100
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clGray
    Font.Height = -16
    Font.Name = 'Arial Narrow'
    Font.Style = []
    ParentFont = False
    TabOrder = 2
    OnClick = Button3Click
  end
  object Memo2: TMemo
    Left = 448
    Top = 102
    Width = 317
    Height = 201
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clGray
    Font.Height = -16
    Font.Name = 'Arial Narrow'
    Font.Style = []
    ParentFont = False
    ScrollBars = ssVertical
    TabOrder = 4
  end
  object trckbr1: TTrackBar
    Left = 606
    Top = 322
    Width = 153
    Height = 33
    Ctl3D = True
    Max = 5
    Min = 1
    ParentCtl3D = False
    Position = 1
    TabOrder = 5
    OnChange = trckbr1Change
  end
  object Edit1: TEdit
    Left = 34
    Top = 54
    Width = 409
    Height = 33
    AutoSize = False
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clGray
    Font.Height = -16
    Font.Name = 'Arial Narrow'
    Font.Style = []
    ParentFont = False
    ReadOnly = True
    TabOrder = 3
  end
  object btn1: TButton
    Left = 673
    Top = 54
    Width = 90
    Height = 33
    Caption = #1042#1099#1093#1086#1076
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clGray
    Font.Height = -16
    Font.Name = 'Arial Narrow'
    Font.Style = []
    ParentFont = False
    TabOrder = 6
    OnClick = btn1Click
  end
  object Button2: TButton
    Left = 864
    Top = 560
    Width = 75
    Height = 25
    Caption = 'Button2'
    TabOrder = 7
    OnClick = Button2Click
  end
  object Button4: TButton
    Left = 328
    Top = 16
    Width = 75
    Height = 25
    Caption = #1054#1089#1090#1072#1085#1086#1074#1080#1090#1100
    TabOrder = 8
    OnClick = Button4Click
  end
  object txtrycn1: TTextTrayIcon
    CycleInterval = 0
    Icon.Data = {
      0000010001001010040000000000280100001600000028000000100000002000
      0000010004000000000080000000000000000000000000000000000000000000
      000000008000008000000080800080000000800080008080000080808000C0C0
      C0000000FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF00FFFF
      FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
      FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
      FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
      FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000
      0000000000000000000000000000000000000000000000000000000000000000
      000000000000000000000000000000000000000000000000000000000000}
    IconIndex = 0
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = []
    Border = False
    Options.OffsetX = 0
    Options.OffsetY = 0
    Options.LineDistance = 0
    Left = 944
    Top = 560
  end
  object CoolTrayIcon1: TCoolTrayIcon
    CycleInterval = 0
    Icon.Data = {
      0000010001002020040000000000E80200001600000028000000200000004000
      0000010004000000000000020000000000000000000000000000000000000000
      000000008000008000000080800080000000800080008080000080808000C0C0
      C0000000FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF000000
      0000000000000000000000000000000000000000000000000000000000000000
      0000000000000000000000000000000000000000000000000000000000000000
      00000000000000000000000000000788888888888888888888888888870007FF
      FFFFFFFFFFFFFFFFFFFFFFFFF70007FFFFFFFFFFFFFFFFFFFFFFFFFFF70007F7
      666266666662FF888888FFFFF70007F8777777777776FFFFFFFFFFFFF70007F8
      777773767776FF888888FFFFF70007F8777777777676FF888888FFFFF70007F8
      667777733766FF888888FFFFF70007F8777777777376FFFFFFFFFFFFF70007F8
      777677777732FFFFFFFFF677F70007F8777777777776FF888888F777F70007F8
      777776777776FF888888F776F70007F8777777767776FFFFFFFFF777F70007F8
      777777776676FF888888F777F70007F8777777777776FF888888F777F70007F8
      776666767776FF888888F777F70007F8757777777776FFFFFFFFF777F70007F8
      667655667776FF888888F777F70007F8888888888888FF888888F777F70007FF
      FFFFFFFFFFFFFFFFFFFFFFFFF70007FFFFFFFFFFFFFFFFFFFFFFFFFFF7000788
      8888888888888888888888888700078888888888888888888876878677000000
      0000000000000000000000000000000000000000000000000000000000000000
      000000000000000000000000000000000000000000000000000000000000FFFF
      FFFFFFFFFFFFFFFFFFFF80000001800000008000000080000000800000008000
      0000800000008000000080000000800000008000000080000000800000008000
      0000800000008000000080000000800000008000000080000000800000008000
      000080000000800000008000000080000000FFFFFFFFFFFFFFFFFFFFFFFF}
    IconIndex = 0
    Left = 984
    Top = 560
  end
  object Timer1: TTimer
    OnTimer = Timer1Timer
    Left = 1184
    Top = 552
  end
end
