using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace EntityRelations.Models
{
    [Table("Address")]
    public class Address
    {
        [Key]
        public int Id { get; set; }
        public string Text { get; set; }
        
        [ForeignKey("Student")]
        public int StudentId { get; set; }
        public virtual Student Student { get; set; }
    }
}