unit Unit1;

interface

uses
   Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
   Dialogs, StdCtrls, XPMan, Agg2D, jpeg, FileCtrl, ExtCtrls, ComCtrls,
  CoolTrayIcon, TextTrayIcon, MMSystem;

type
   TSomeThread = class(tthread)
   private
      s: string;
      Stop: Boolean;
      Busy: integer;
      procedure addstr(TT: string);
      procedure threadwork;
   protected
      procedure execute; override;
      procedure Convert(SS: string);
   end;

   TForm1 = class(TForm)
      Button1: TButton;
      Memo1: TMemo;
      Button3: TButton;
      Edit1: TEdit;
      Memo2: TMemo;
    Label1: TLabel;
    Label2: TLabel;
    trckbr1: TTrackBar;
    lbl4: TLabel;
    btn1: TButton;
    txtrycn1: TTextTrayIcon;
    CoolTrayIcon1: TCoolTrayIcon;
    Label3: TLabel;
    Timer1: TTimer;
    Label4: TLabel;
    Button2: TButton;
    Button4: TButton;
      procedure Button1Click(Sender: TObject);
      procedure Button3Click(Sender: TObject);
    procedure lbl3Click(Sender: TObject);
    procedure trckbr1Change(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure btn1Click(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure Button4Click(Sender: TObject);
   private
      { Private declarations }
   public
      Threads: Integer;
      { Public declarations }
   end;

var
   Form1: TForm1;
   firstThread, secondThread, Thread3: TSomeThread;
   en,col: integer;
   enn, stop:Boolean;
   StartTime: TTime;
   a: Boolean;
implementation

{$R *.dfm}

function GetFileCount(Dir: string):integer;
var
  fs: TSearchRec;
  pics: Integer;
begin
  pics:=0;
  if FindFirst(Dir+'\*.jpg', faAnyFile - faDirectory - faVolumeID, fs) = 0
    then
    repeat
      inc(pics);
    until
      FindNext(fs) <> 0;
  FindClose(fs);

Result := Pics;   //вот это добавить надо
end;

procedure TSomeThread.Convert(SS: string);
var
   B: TBitmap;
   VG: TAgg2D;
   jpeg: TJPEGImage;
   i, j: integer;
   Img: TPicture;
   c1,c2,c3: TAggColor;
   q:string;
begin
   addstr('!!!»нициализаци€ графических обьектов...');
   Img := TPicture.Create;

   //—оздаем JPEG
   jpeg := TJPEGImage.Create;
   jpeg.CompressionQuality := 100; {уровень компрессии - 100 наилучшее качество}
   jpeg.LoadFromFile(SS);

   //—оздаем экземпл€р BMP
   B := TBitmap.Create;
   B.Width := jpeg.Width;
   B.Height := jpeg.Height;
   B.PixelFormat := pf32bit;

   //ѕереносим картинку из JPG в BMP
   addstr('”становка св€зи с исходным изображением: ' + SS);
   B.Assign(jpeg);

   Img.Bitmap.PixelFormat := pf32bit;

   VG := TAgg2D.Create;

   if VG.Attach(B) then
   begin
      addstr('–исуем вод€ной знак...');

      VG.LineColor($00, $00, $8B, 190);
      VG.Font('Times New Roman', 80);
      VG.Text(b.Width - 400, b.Height - 30, 'delphi');
      VG.FillColor(255, 255, 0, 255);
      VG.Ellipse(b.Width - 80, b.Height - 50, 50, 50);
      VG.FillColor(0, 0, 0, 255);
      VG.Ellipse(b.Width - 50 - 50, b.Height - 20 - 50, 10, 10);
      VG.Ellipse(b.Width - 50 - 50 + 50, b.Height - 20 - 50, 10, 10);
      vg.Ellipse(b.Width - 50 - 50+ 30, b.Height - 20 - 10, 10, 10);
      VG.LineWidth(2);
      // Upside-down Text
      VG.FlipText(true);
      VG.LineColor($C0, $C0, $C0, 90);
      VG.FillColor(0,0,0,130);
      VG.Font('Times New Roman', 80);
      VG.Text(b.Width - 400, b.Height - 30, 'delphi');
   end;

   addstr('—охран€ем готовое изображение...');
   Img.Bitmap.Assign(B);
   //—охран€ем
   jpeg.Assign(B);

   q:=SS;
   insert('(1)',q,Length(q)-4);
   jpeg.SaveToFile(q);

   VG.Free;
   jpeg.Free;
   Img.Free;
   B.Free;

end;

procedure TSomeThread.execute;
begin
   inherited;

   Busy := 1;
   Synchronize(threadwork);

   Convert(S);
   Busy := -1;
   Synchronize(threadwork);
   Terminate;

   Dec(en);
   if en<col then enn:=False;
end;

procedure TSomeThread.threadwork;
begin
   form1.Threads := form1.Threads + Busy;
   Form1.Label2.Caption := IntToStr(form1.Threads);
end;

procedure TSomeThread.addstr(TT: string);
begin
   form1.Memo2.lines.add(TT);
end;

procedure TForm1.Button1Click(Sender: TObject);
var
   code: LongInt;
   i, n: integer;
begin
   {
   tpIdle Ч низший приоритет. ѕоток получает врем€ только тогда, когда операционна€ система находитс€ в состо€нии просто€.
   tpLowest Ч приоритет на два пункта ниже нормального.
   tpLower Ч приоритет на один пункт ниже нормального.
   tpNormal Ч нормальный приоритет.
   tpHigher Ч приоритет на один пункт выше нормального.
   tpHighest Ч приоритет на два пункта выше нормального.
   tpTimeCritical Ч максимальный приоритет. ѕриоритет на уровне функций €дра операционной системы.
   }
   StartTime:= Now;
   Timer1.Enabled:= True;
   n := 0;
   while (n < memo1.Lines.Count) and (stop = False) do
   begin
      Application.ProcessMessages;

      if (not(enn)) and (en<col) then
      begin
         firstThread := TSomeThread.create(true);
         firstThread.freeonterminate := true;
         firstThread.s := Memo1.Lines.Strings[n];
         firstThread.priority := tpNormal;

         inc(n);

         firstThread.resume;

         Inc(en);
         if col=en then enn:=True;
      end;
   end;
   CoolTrayIcon1.ShowHint := True;
   CoolTrayIcon1.MinimizeToTray := True;
   CoolTrayIcon1.IconVisible := True;
   CoolTrayIcon1.HideBalloonHint;
   CoolTrayIcon1.HideTaskbarIcon;
   CoolTrayIcon1.ShowBalloonHint('¬нимание', 'ќбработка успешно выполнена' + #13, bitWarning, 10);
   Timer1.Enabled:=false;

end;

procedure TForm1.Button3Click(Sender: TObject);
var
   B: TBitmap;
   VG: TAgg2D;
   jpeg: TJPEGImage;
   searchResult: TSearchRec;
   imageDirectory, imageFilePath, outputDirectory, outputImagePath, SelectedFolder, SelecteToSave: string;
   c1, c2: TAggColor;
   fileCount:Integer;

begin
   SelectDirectory('¬ыберите папку', '', SelectedFolder);
   imageDirectory := SelectedFolder;
   label3.caption:= imageDirectory;
   Edit1.Text := imageDirectory;
   fileCount := GetFileCount(imageDirectory);
   Label3.Caption := ' ол-во файлов: ' + IntToStr(fileCount);

   memo1.Lines.Clear;
   button1.Enabled:=True;
   if FindFirst(IncludeTrailingPathDelimiter(imageDirectory) + '*.jpg', faAnyFile, searchResult) = 0 then
   begin
      repeat
         imageFilePath := IncludeTrailingPathDelimiter(imageDirectory) + searchResult.Name;
         memo1.Lines.Add(imageFilePath);

      until FindNext(searchResult) <> 0;
      FindClose(searchResult);
   end;
end;

procedure TForm1.lbl3Click(Sender: TObject);
begin
close;
end;

procedure TForm1.trckbr1Change(Sender: TObject);
begin
lbl4.Caption:=IntToStr(trckbr1.Position);
col:=trckbr1.Position;
end;

procedure TForm1.FormShow(Sender: TObject);
begin
form1.Top:=0;
end;

procedure TForm1.btn1Click(Sender: TObject);
begin
Close;
end;

procedure TForm1.Timer1Timer(Sender: TObject);
begin
Label4.Caption:= FormatDateTime('hh:nn:ss',Now-StartTime);
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
trckbr1.Position := trckbr1.Position+1;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
Button2Click(sender);
stop:= False;
a := True;
end;


procedure TForm1.Button4Click(Sender: TObject);

begin
if a = True then
begin
stop:= True ;
a:= false;
end
else
begin
stop:=False;
a:= true;
Button1Click(Sender);
end;
end;

end.

