
public class Member {
    private String name;
    private String memberId;
    private String contact;

    public Member(String name, String memberId, String contact) {
        this.name = name;
        this.memberId = memberId;
        this.contact = contact;
    }

    // Getters and setters for fields
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        this.memberId = memberId;
    }

    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    @Override
    public String toString() {
        return "Member{" +
                "name='" + name + '\'' +
                ", memberId='" + memberId + '\'' +
                ", contact='" + contact + '\'' +
                '}';
    }
}

