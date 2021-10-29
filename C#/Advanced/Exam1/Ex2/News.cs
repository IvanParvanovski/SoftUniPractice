namespace Ex2
{
    public class News
    {
        public string Title { get; set; }
        public string Text { get; set; }
        public string Writer { get; set; }

        public News(string title, string text, string writer)
        {
            this.Title = title;
            this.Text = text;
            this.Writer = writer;
        }

        public void Edit(string newText)
        {
            this.Text = newText;
        }

        public void ChangeWriter(string newWriter)
        {
            this.Writer = newWriter;
        }

        public void Rename(string newTitle)
        {
            this.Title = newTitle;
        }

        public override string ToString()
        {
            return $"{this.Title} - {this.Text}: {this.Writer}";
        }
    }
    
}