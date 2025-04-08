from django.contrib.auth.models import User
from django.db import models


# Model to represent a Question
class Question(
    models.Model,
):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


# Model to represent an Answer
class Answer(
    models.Model,
):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
    )
    content = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Answer by {self.created_by.username} to {self.question.title}"


# Model to represent a Like on an Answer
class Like(
    models.Model,
):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = (
            'answer',
            'user'
        )

    def __str__(self):
        return f"Like by {self.user.username} on {self.answer.content[:20]}"
