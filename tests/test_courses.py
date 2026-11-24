import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(yandex_page_with_state: Page):
        
        yandex_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = yandex_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        no_results_title = yandex_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_title).to_be_visible()
        expect(no_results_title).to_have_text("There is no results")

        empty_list_icon = yandex_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_list_icon).to_be_visible()

        empty_description_title = yandex_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_description_title).to_be_visible()
        expect(empty_description_title).to_have_text("Results from the load test pipeline will be displayed here")