# Anki Flashcards Collection

A curated collection of Anki flashcards for technical topics, organized by subject area.

## 📁 Structure

```
anki-flashcards/
├── README.md
├── databases/
│   └── sql-server/
│       ├── sql_data_engineering_warehouse_flashcards.txt
│       └── sql_server_database_engineering_flashcards.txt
├── data-engineering/
├── data-warehousing/
├── devops/
├── programming/
├── cloud/
├── security/
└── architecture/
```

## 🎯 Topics Covered

### Databases
- **SQL Server Database Engineering** - DBA-focused knowledge (backup/recovery, HA/DR, monitoring)
- **SQL Data Engineering & Warehousing** - Development-focused (stored procedures, warehouse design, ETL patterns)

## 📥 How to Import into Anki

1. **Open Anki** and select the deck you want to add to (or create a new one)
2. Go to **File → Import**
3. Select the `.txt` flashcard file
4. Configure import settings:
   - **Note type**: Basic (or your preferred type)
   - **Field separator**: Configure based on the file format
   - **Deck**: Select your target deck
   - **Fields mapped to**: 
     - Field 1 → Front (Question)
     - Field 2 → Back (Answer)
5. Click **Import**

## 📝 Flashcard Format

Cards follow this pattern:
```
**Question: What is...?**
**Answer:** Detailed explanation here...

---
```

Each card is separated by `---`

## 🚀 Adding New Flashcards

1. Create new `.txt` files following the naming convention: `topic_subtopic_flashcards.txt`
2. Follow the established format with clear questions and comprehensive answers
3. Place files in the appropriate subdirectory
4. Update this README with the new topic

## 💡 Tips for Effective Flashcards

- **Keep questions specific** - One concept per card
- **Include examples** - Code snippets, real-world scenarios
- **Link concepts** - Reference related cards when applicable
- **Review regularly** - Spaced repetition is key to retention
- **Update cards** - As your knowledge grows, refine answers

## 🔧 Anki Add-ons for Code

Recommended add-ons for technical flashcards:
- **Syntax Highlighting for Code** - Better code readability
- **Image Occlusion Enhanced** - For diagrams and visual concepts
- **Hierarchical Tags** - Better organization
- **Pop-up Dictionary** - Quick reference

## 📊 Progress Tracking

Consider using Anki's statistics to:
- Monitor review consistency
- Identify difficult topics
- Adjust card intervals
- Focus on weak areas

## 🤝 Contributing

To add new flashcard sets:
1. Follow the existing format and structure
2. Test import in Anki before committing
3. Update the README with new topics
4. Include import instructions if the format differs

## 📚 Additional Resources

- [Anki Manual](https://apps.ankiweb.net/docs/manual.html)
- [Anki Web](https://ankiweb.net/) - Sync across devices
- [Awesome Anki](https://github.com/tessen/awesome-anki) - Community resources

---

*Created to support continuous learning in technical fields*