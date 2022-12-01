using System.Collections;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore;

namespace EntityRelations.Models
{
    [Table("Student")]
    public class Student
    {
        [Key]
        public int Id { get; set; }
        
        [MaxLength(100)]
        public string Name { get; set; }
        
        [ForeignKey("Address")]
        public int AddressId { get; set; }
        
        // public virtual Address Address { get; set; }
        public virtual ICollection<Address> Addresses { get; set; } 
        
    }
}